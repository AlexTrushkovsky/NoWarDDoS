from functools import lru_cache
from pathlib import Path
from typing import List

from pydantic import BaseSettings

_DEFAULT_DOTENV_FILE = Path(".env").resolve()
_DEFAULT_SITES_HOSTS = ["https://raw.githubusercontent.com/opengs/uashieldtargets/master/sites.json"]
_DEFAULT_PROXIES_HOSTS = ["https://raw.githubusercontent.com/xfreed/Proxy-List/main/Proxy_Http.txt"]
_UPDATE_URL = \
    "https://gist.githubusercontent.com/AlexTrushkovsky/041d6e2ee27472a69abcb1b2bf90ed4d/raw/nowarversion.json"


class Settings(BaseSettings):
    VERSION: int = 7
    SITES_HOSTS: List[str] = _DEFAULT_SITES_HOSTS
    PROXIES_HOSTS: List[str] = _DEFAULT_PROXIES_HOSTS
    MAX_REQUESTS_TO_SITE: int = 200
    TARGET_UPDATE_RATE: int = 600

    # tor settings
    ENABLE_TOR: bool = False
    TOR_PORT: int = 9051
    TOR_PASSWORD: str = ''
    TOR_CONTROL_PORT: int = 9050
    TOR_HOST: str = '127.0.0.1'
    READ_TIMEOUT: int = 10
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

@lru_cache()
def get_settings():
    return Settings(_env_file=_DEFAULT_DOTENV_FILE)
