from os import getenv
from typing import List
from distutils.util import strtobool
from pydantic import BaseSettings
from functools import lru_cache
from pathlib import Path

_DEFAULT_DOTENV_FILE = Path("./.env").resolve()
_DEFAULT_SITES_HOSTS = ["https://raw.githubusercontent.com/opengs/uashieldtargets/master/sites.json"]
_DEFAULT_PROXIES_HOSTS = ["https://raw.githubusercontent.com/opengs/uashieldtargets/master/proxy.json"]
_UPDATE_URL = \
    "https://gist.githubusercontent.com/AlexTrushkovsky/041d6e2ee27472a69abcb1b2bf90ed4d/raw/nowarversion.json"


class Settings(BaseSettings):
    VERSION: int = 7
    SITES_HOSTS: List[str] = getenv("SITES_HOSTS", _DEFAULT_SITES_HOSTS)
    PROXIES_HOSTS: List[str] = getenv("PROXIES_HOSTS", _DEFAULT_PROXIES_HOSTS)
    MAX_REQUESTS_TO_SITE: int = int(getenv('MAX_REQUESTS_TO_SITE', 200))
    DEFAULT_THREADS: int = int(getenv('DEFAULT_THREADS', 500))
    TARGET_UPDATE_RATE: int = int(getenv('TARGET_UPDATE_RATE', 600))

    # tor settings
    ENABLE_TOR: bool = strtobool(getenv("ENABLE_TOR", "false"))
    TOR_PORT: int = int(getenv("TOR_PORT", 9051))
    TOR_PASSWORD: str = getenv("TOR_PASSWORD", None)
    TOR_CONTROL_PORT: int = int(getenv("TOR_CONTROL_PORT", 9050))
    TOR_HOST: str = getenv("TOR_HOST", "127.0.0.1")

    READ_TIMEOUT: int = 10
    SUPPORTED_PLATFORMS: dict = {
        'linux': 'Linux'
    }
    UPDATE_URL: str = _UPDATE_URL
    BROWSER: dict = {'browser': 'firefox', 'platform': 'android', 'mobile': True}
    HEADERS_TEMPLATE: dict = {
        'Content-Type': 'application/json',
        'cf-visitor': 'https',
        'User-Agent': None,
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru',
        'x-forwarded-proto': 'https',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    class Config:
        dotenv_path = _DEFAULT_DOTENV_FILE


@lru_cache()
def get_settings():
    return Settings(_env_file=_DEFAULT_DOTENV_FILE)
