from cloudscraper import create_scraper
from stem.control import Controller
from stem import Signal
from settings import get_settings

settings = get_settings()


class TorProxy:
    def __init__(self, port=9051, host='127.0.0.1', control_port=9050, password=None):
        self._host = host
        self._port = port
        self._control_port = control_port
        self._password = password

    def get_sock5_proxies(self) -> dict:
        return {
            "https": f"socks5://{self._host}:{self._control_port}",
            "http": f"socks5://{self._host}:{self._control_port}"
        }

    def change_ip(self):
        with Controller.from_port(port=self._port) as controller:
            controller.authenticate(password=self._password)
            controller.signal(Signal.NEWNYM)
            controller.close()

    def get_ip(self):
        scrapper = create_scraper(browser=settings.BROWSER)
        scrapper.proxies.update(self.get_sock5_proxies())
        try:
            return scrapper.get("http://httpbin.org/ip").json()['origin']
        except Exception:
            return "0.0.0.0"
