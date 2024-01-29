'''Module defines the base common settings for the whole package'''

from argparse import Namespace

BASE_URL = "https://statsapi.mlb.com/api"
MAX_RETRIES = 3
TIMEOUT = 30 # seconds

TOKEN_LIFETIME = 1 * 60 * 60 # 1 hour

DEFAULT_CONFIG_PATH = "~/.mlb/config"
ENVIRONMENT_VARIABLES = Namespace(
    EMAIL = "MLB_SDK_EMAIL",
    PASSWORD = "MLB_SDK_PASSWORD",
    CONFIG_PATH = "MLB_SDK_CONFIG_PATH",
)
