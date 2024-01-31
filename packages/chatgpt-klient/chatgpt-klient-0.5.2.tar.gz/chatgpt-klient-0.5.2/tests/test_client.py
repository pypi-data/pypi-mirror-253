import pytest
import json
from pathlib import Path
from chatgpt_klient.consts import ROOT_DIR, ENGINES, DEFAULT_ENGINES
from chatgpt_klient.client import ChatGPTPrompt


@pytest.fixture
def config():
    config_f = ROOT_DIR.joinpath("config.json")
    return json.loads(config_f.read_text())


@pytest.mark.parametrize("model", ENGINES.keys())
def test_ChatGPTPrompt_init_all_models_OK(model, config):
    ChatGPTPrompt(api_key=config["openai_key"], engine=model)


@pytest.mark.parametrize("model", DEFAULT_ENGINES.keys())
def test_ChatGPTPrompt_init_default_models_OK(model, config):
    ChatGPTPrompt(api_key=config["openai_key"], engine=model)


def test_ChatGPTPrompt_init_nomodel_OK(config):
    ChatGPTPrompt(api_key=config["openai_key"])


@pytest.mark.parametrize("model", ["gpt4", "ronaldo"])
def test_ChatGPTPrompt_init_bad_model_FAIL(model, config):
    with pytest.raises(Exception):
        ChatGPTPrompt(api_key=config["openai_key"], engine=model)


@pytest.mark.parametrize("model", DEFAULT_ENGINES.keys())
def test_ChatGPTPrompt_init_bad_apikey_FAIL(model):
    with pytest.raises(Exception):
        ChatGPTPrompt(api_key="roberta", engine=model)


@pytest.mark.parametrize("model", DEFAULT_ENGINES.keys())
def test_send_prompt(model, config):
    prompter = ChatGPTPrompt(api_key=config["openai_key"], engine=model)
    r = prompter.send_prompt("hola caracola")
    print(f"Response: {r}")
    assert isinstance(r, str)


@pytest.mark.parametrize("model", DEFAULT_ENGINES.keys())
def test_send_prompt_streaming(model, config):
    prompter = ChatGPTPrompt(api_key=config["openai_key"], engine=model)
    r = prompter.send_prompt("hola caracola", stream=True)
    for token in r:
        assert isinstance(token, str)
