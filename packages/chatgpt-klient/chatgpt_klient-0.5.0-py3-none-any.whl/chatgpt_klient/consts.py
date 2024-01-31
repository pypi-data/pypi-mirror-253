from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent.parent

NO_AUTH_MSG = """
For this script to work, authentication to OpenAI is needed. This should be provided in one of the following 3 ways:
    1. Pass valid authentication data via the --key option.
    2. Use the --config option to point to a valid JSON with the "api_key" field.
    3. Set the environment variable OPENAI_CONFIGFILE pointing to a valid JSON file with the "api_key" field.
"""

INVALID_JSON_MSG = """
The config file should be in a valid JSON format like the following:
{
    "api_key": "dk39??!meerLq"
}
"""


ENGINES = {
    "babbage-002": {
        "type": "legacy",
        "max_tokens": 16384,
    },
    "davinci-002": {
        "type": "legacy",
        "max_tokens": 16384,
    },
    "gpt-4": {
        "type": "chat",
        "max_tokens": 8192,
    },
    "gpt-3.5-turbo": {
        "type": "chat",
        "max_tokens": 4096,
    },
    "gpt-3.5-turbo-16k": {
        "type": "chat",
        "max_tokens": 16384,
    },
    # 2023-11-07: Nuevas incorporaciones
    "gpt-4-1106-preview": {
        "type": "chat",
        "max_tokens": 128000,
        "max_output_tokens": 4096,
    },
    "gpt-4-vision-preview": {
        "type": "chat",
        "max_tokens": 128000,
        "max_output_tokens": 4096,
    },
    "gpt-3.5-turbo-1106": {
        "type": "chat",
        "max_tokens": 16384,
        "max_output_tokens": 4096,
    },
}

DEFAULT_ENGINES = {
    "gpt3.5-default": "gpt-3.5-turbo-1106",
    "gpt4-default": "gpt-4-1106-preview",
}

MAX_DELAY = 500
CLIENT_TIMEOUT = 300
DEFAULT_AZURE_API_VERSION = "2023-05-15"
DEFAULT_AZURE_ENDPOINT = "https://azureaistudio-swedencentral.openai.azure.com/"
DEFAULT_AZURE_ENGINE = DEFAULT_ENGINES["gpt3.5-default"]
