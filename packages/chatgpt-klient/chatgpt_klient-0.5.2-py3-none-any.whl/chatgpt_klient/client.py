import copy
from openai import OpenAI, AzureOpenAI
from openai import RateLimitError, APITimeoutError, BadRequestError
import math
import time
import tiktoken
import time
from typing import Generator, Union, Literal
from logutils import get_logger
from chatgpt_klient.consts import (
    MAX_DELAY,
    ENGINES,
    DEFAULT_ENGINES,
    CLIENT_TIMEOUT,
    DEFAULT_AZURE_API_VERSION,
    DEFAULT_AZURE_ENDPOINT,
)
from chatgpt_klient.exceptions import (
    InvalidAPIKeyError,
    InvalidModelError,
    InvalidResponseError,
)
from rich.console import Console

logger = get_logger("chatgpt_client")
console = Console()


class ChatGPTPrompt:
    def __init__(
        self,
        api_key,
        engine="gpt3.5-default",
        cap_tokens=math.inf,
        service: Literal["openai", "azure"] = "openai",
        azure_api_version: str = DEFAULT_AZURE_API_VERSION,
        azure_endpoint: str = DEFAULT_AZURE_ENDPOINT,
        azure_instance: str | None = None,
    ):
        self.api_key = api_key
        self.service = service
        if self.service == "openai":
            logger.info(f"Initializing an OpenAI {engine} engine")
            self.openai = OpenAI(api_key=self.api_key, timeout=CLIENT_TIMEOUT)
        elif self.service == "azure":
            if azure_instance is None:
                raise NoAzureInstanceError
            logger.info(
                f"Initializing an Azure connection to the {azure_instance} instance (model {engine})"
            )
            self.openai = AzureOpenAI(
                api_key=api_key,
                api_version=azure_api_version,
                azure_endpoint=azure_endpoint,
            )

        self.msg_history = {"messages": [], "tokens": []}
        self.last_prompt_tokens = 0
        self.cap_tokens = cap_tokens
        self.set_engine(engine, azure_instance)
        self.check_api_key_validity()

    def list_models(self):
        return list(ENGINES.keys()) + list(DEFAULT_ENGINES.keys())

    def check_api_key_validity(self):
        try:
            if self.service == "openai":
                r = self.openai.completions.create(
                    model="davinci-002",
                    prompt="Hi",
                    max_tokens=5,
                ).model_dump()
            elif self.service == "azure":
                r = self.openai.chat.completions.create(
                    model=self.engine,
                    messages=[{"role": "user", "content": "Hola!"}],
                    max_tokens=5,
                    stream=False,
                ).model_dump()
            r = self.check_response_validity(r)
        except Exception:
            logger.exception("Invalid API key.")
            raise InvalidAPIKeyError(
                "Your API key does not seem to be valid. Please check it."
            )
        else:
            logger.info("API key seems valid and working.")

    def check_model_validity(self):
        if self.real_engine not in self.list_models():
            logger.error(f"Engine {self.real_engine} is not supported")
            raise InvalidModelError(f"Engine {self.real_engine} not supported")
        elif self.engine is None:
            raise InvalidModelError("No engine instance")
        try:
            if self.real_engine in [
                k for k, v in ENGINES.items() if v["type"] == "legacy"
            ]:
                r = self.openai.completions.create(
                    model=self.engine,
                    prompt="Hi",
                    max_tokens=5,
                ).model_dump()
                r = self.check_response_validity(r)
            elif self.real_engine in [
                k for k, v in ENGINES.items() if v["type"] == "chat"
            ]:
                r = self.openai.chat.completions.create(
                    model=self.engine,
                    messages=[{"role": "user", "content": "Hi"}],
                    max_tokens=5,
                ).model_dump()
                r = self.check_response_validity(r)
                logger.debug(
                    f'Model validity test: {r["choices"][0]["message"]["content"]}'
                )
            else:
                raise InvalidModelError(f"Engine {self.engine} not supported")
        except Exception:
            logger.info(f"Invalid model ({self.engine}) for your API key")
            raise InvalidModelError(f"Engine {self.engine} not supported")
        else:
            logger.info(f"Model ({self.engine}) seems to be valid.")

    def check_response_validity(self, r) -> dict:
        try:
            match r:
                case {"choices": [{"text": str()}]}:
                    pass
                case {"choices": [{"message": {"content": str()}}]}:
                    pass
                case _:
                    raise InvalidModelError
        except Exception:
            raise InvalidResponseError(f"Response is not well formed: {r}")
        else:
            logger.debug("Response seems to be well formed")
            return r

    def set_engine(self, engine: str, azure_instance: str | None = None):
        if engine in DEFAULT_ENGINES.keys():
            self.real_engine = DEFAULT_ENGINES[engine]
        else:
            self.real_engine = engine
        if self.service == "openai":
            self.engine = self.real_engine
            self.azure_instance = None
        elif self.service == "azure":
            if azure_instance is None:
                raise NoAzureInstanceError("Azure API requires passing an instance")
            self.engine = azure_instance
            self.azure_instance = azure_instance
        self.check_model_validity()
        self.encoding = tiktoken.encoding_for_model(self.real_engine)
        eng_attrs = ENGINES[self.real_engine]
        if "max_output_tokens" in eng_attrs:
            self.max_tokens = eng_attrs["max_tokens"] - eng_attrs["max_output_tokens"]
        else:
            self.max_tokens = int(eng_attrs["max_tokens"] / 2)

    def set_system_directive(self, directive: str):
        self.clean_history(keep_sysdir=False)
        self.msg_history["messages"].append(
            {
                "role": "system",
                "content": directive,
            }
        )
        self.msg_history["tokens"].append(len(self.encoding.encode(directive)))

    def clean_history(self, keep_sysdir=True):
        new_history = {"messages": [], "tokens": []}
        if keep_sysdir:
            for i, m in enumerate(self.msg_history["messages"]):
                if m["role"] == "system":
                    new_history["messages"].append(
                        {"role": m["role"], "content": m["content"]}
                    )
                    new_history["tokens"].append(self.msg_history["tokens"][i])
        self.msg_history = new_history
        self.last_prompt_tokens = 0

    def get_max_tokens_allowed(self):
        return (
            min(
                [
                    self.max_tokens,
                    ENGINES[self.real_engine]["max_tokens"],
                    self.cap_tokens,
                ]
            )
            - 10
        )

    def get_max_output_tokens_allowed(self):
        aux = math.inf
        if "max_output_tokens" in ENGINES[self.real_engine]:
            aux = ENGINES[self.real_engine]["max_output_tokens"]
        return min(self.get_max_tokens_allowed(), aux)

    def calculate_prompt_tokens(self, text, no_history=True, keep_sysdir=False):
        aux_history = copy.deepcopy(self.msg_history)
        aux_last_prompt = self.last_prompt_tokens
        if no_history:
            self.clean_history(keep_sysdir=keep_sysdir)
        self.msg_history["messages"].append(
            {
                "role": "user",
                "content": text,
            }
        )
        self.msg_history["tokens"].append(len(self.encoding.encode(text)))
        potential_tokens = self.msg_history["tokens"][-1] + self.last_prompt_tokens
        self.msg_history = aux_history
        self.last_prompt_tokens = aux_last_prompt
        return potential_tokens

    def send_prompt(
        self, text: str, no_history: bool = False, stream: bool = False
    ) -> Union[str, Generator[str, None, None]]:
        """
        Send a prompt to ChatGPT with some text to get a response.

        :param text: the text to be sent as a prompt. This will be appended as the
          latest "user" message of the conversation
        :param no_history: deactivate the use of a previous history of messages. If
          set to True, all previous messages will be cleared and only the one in
          *text* will be used
        :param stream: set to True to return the generated tokens synchronously, one
          by one as we receive them from ChatGPT. Otherwise, the text will be returned
          as a whole once it is ready.
        :returns: either a string with the whole text, or a generator of the tokens
          composing the text
        """
        response = "No response"
        if self.real_engine in [k for k, v in ENGINES.items() if v["type"] == "legacy"]:
            r = self.openai.completions.create(
                model=self.engine,
                prompt=text,
                max_tokens=self.get_max_output_tokens_allowed(),
            ).model_dump()
            r = self.check_response_validity(r)
            response = r["choices"][0]["text"]
        elif self.real_engine in [k for k, v in ENGINES.items() if v["type"] == "chat"]:
            if no_history:
                self.clean_history()
            self.msg_history["messages"].append(
                {
                    "role": "user",
                    "content": text,
                }
            )
            self.msg_history["tokens"].append(len(self.encoding.encode(text)))
            self.reduce_msg_history(text)
            if stream:
                return self.chat_completion_stream(text)
            else:
                return self.chat_completion_no_stream(text)
        else:
            logger.warning(f"Engine {self.engine} not supported")
        return response

    def interactive_prompt(self, system_directive: str | None = None):
        if system_directive:
            self.set_system_directive(system_directive)
        console.print("###########", style="bold")
        console.print("# ChatGPT #", style="bold")
        console.print("###########", style="bold")
        console.print(
            f"[bold yellow]Engine:[/bold yellow] {self.engine}", highlight=False
        )
        console.print("[bold cyan]Enter 'q'/'quit' to exit the chat[/]")
        console.print("[bold cyan]Enter anything to start chatting.[/]")
        console.print()
        while True:
            input_text = input("$ ")
            if input_text in ("q", "quit"):
                print("ChatGPT> Sayonara, baby!")
                break
            try:
                r = self.send_prompt(text=input_text)
            except RateLimitError:
                logger.warning("You are sending requests too fast. Delaying 20s...")
                time.sleep(20)
                r = self.send_prompt(text=input_text)

            console.print(f"[bold green]ChatGPT>[/] [green]{r}[/]")

    def reduce_msg_history(self, text: str):
        potential_tokens = self.msg_history["tokens"][-1] + self.last_prompt_tokens
        logger.debug(f"Potential tokens: {potential_tokens}")
        while potential_tokens > self.get_max_tokens_allowed():
            logger.warning("Too many tokens. Reducing history size")
            aux = {"messages": [], "tokens": []}
            first_user = True
            first_assistant = True
            for i in range(len(self.msg_history["messages"])):
                if self.msg_history["messages"][i]["role"] == "user" and first_user:
                    first_user = False
                    potential_tokens -= self.msg_history["tokens"][i]
                elif (
                    self.msg_history["messages"][i]["role"] == "assistant"
                    and first_assistant
                ):
                    first_assistant = False
                    potential_tokens -= self.msg_history["tokens"][i]
                else:
                    aux["messages"].append(self.msg_history["messages"][i])
                    aux["tokens"].append(self.msg_history["tokens"][i])
            self.msg_history = aux
        if text not in [m["content"] for m in self.msg_history["messages"]]:
            raise TooManyTokensError(
                f"The maximum accepted tokens ({self.get_max_tokens_allowed()}) is not big enough to process your prompt"
            )

    def chat_completion_no_stream(self, text: str, delay: int = 5) -> str:
        try:
            r = self.openai.chat.completions.create(
                model=self.engine,
                messages=self.msg_history["messages"],
                max_tokens=self.get_max_output_tokens_allowed(),
                stream=False,
            ).model_dump()
            logger.debug(r)
            r = self.check_response_validity(r)
            self.last_prompt_tokens = r["usage"]["total_tokens"]
            response = r["choices"][0]["message"]["content"]
            if response:
                self.msg_history["messages"].append(
                    {
                        "role": "assistant",
                        "content": response,
                    }
                )
                self.msg_history["tokens"].append(len(self.encoding.encode(response)))
        except RateLimitError:
            logger.warning(f"Rate limit reached, delaying request {delay} seconds")
            if delay > MAX_DELAY:
                raise Exception(
                    "Recurring RateLimitError and delaying requests not working"
                )
            time.sleep(delay)
            return self.chat_completion_no_stream(text, delay=delay * 2)
        except BadRequestError as e:
            if "maximum context length" in str(e):
                self.clean_history(keep_sysdir=True)
                return self.chat_completion_no_stream(text, delay=delay * 2)
            else:
                logger.warning("We shouldn't be getting here!")
                raise e
        except APITimeoutError:
            logger.warning("Request failed with timeout, retrying")
            if delay > MAX_DELAY:
                raise Exception("Getting timeouts to all requests")
            time.sleep(delay)
            return self.chat_completion_no_stream(text, delay=delay * 2)
        else:
            return response

    def chat_completion_stream(
        self, text: str, delay: int = 5
    ) -> Generator[str, None, None]:
        try:
            stream = self.openai.chat.completions.create(
                model=self.engine,
                messages=self.msg_history["messages"],
                max_tokens=self.get_max_output_tokens_allowed(),
                stream=True,
            )
            aux_num_tokens = 0
            aux_text = ""
            for r in stream:
                match chunk := r.choices[0].model_dump():
                    case {"finish_reason": "stop"}:
                        break
                    case {"delta": {"content": token}}:
                        logger.debug(f"Received chunk: {token}")
                        aux_text += token
                        aux_num_tokens += 1
                        yield token
                    case _:
                        logger.warning(f"Strange object structure: {chunk}")
            self.last_prompt_tokens = aux_num_tokens
            self.msg_history["messages"].append(
                {
                    "role": "assistant",
                    "content": aux_text,
                }
            )
            self.msg_history["tokens"].append(len(self.encoding.encode(aux_text)))
        except RateLimitError:
            logger.warning(f"Rate limit reached, delaying request {delay} seconds")
            if delay > MAX_DELAY:
                raise Exception(
                    "Recurring RateLimitError and delaying requests not working"
                )
            time.sleep(delay)
            self.chat_completion_stream(text, delay=delay * 2)
        except BadRequestError as e:
            if "maximum context length" in str(e):
                self.clean_history(keep_sysdir=True)
                self.chat_completion_stream(text, delay=delay * 2)
            else:
                logger.warning("We shouldn't be getting here!")
                raise e
        except APITimeoutError:
            logger.warning("Request failed with timeout, retrying")
            if delay > MAX_DELAY:
                raise Exception("Getting timeouts to all requests")
            time.sleep(delay)
            self.chat_completion_stream(text, delay=delay * 2)


class TooManyTokensError(Exception):
    pass


class NoAzureInstanceError(Exception):
    pass
