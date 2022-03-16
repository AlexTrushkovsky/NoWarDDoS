import json
from urllib.parse import unquote

import cachetools.func
import cloudscraper

from settings import get_settings

settings = get_settings()


class RemoteProvider:
    def __init__(self, targets=None):
        self.targets = [unquote(target) for target in targets] if targets else None
        self._proxies = []
        self.sites = []
        self.scraper = cloudscraper.create_scraper(
            browser=settings.BROWSER,
        )

    def _scrap_json(self, link):
        content = self.scraper.get(link).content
        try:
            data = json.loads(content)
            return data
        except json.decoder.JSONDecodeError:
            return []

    @cachetools.func.ttl_cache(ttl=settings.TARGET_UPDATE_RATE)
    def get_target_sites(self):
        if self.targets:
            self.sites = self.targets
        else:
            self.sites = []
            for host in settings.SITES_HOSTS:
                try:
                    data = self._scrap_json(host)
                    self.sites.extend([site.get("page") for site in data])
                except Exception:
                    pass
        return list(set(self.sites))

    def _parse_text(self, link):
        content = self.scraper.get(link).content.decode("utf-8")
        return content.split("\n")

    @cachetools.func.ttl_cache(ttl=settings.TARGET_UPDATE_RATE)
    def get_proxies(self):
        for link in settings.PROXIES_HOSTS:
            try:
                self._proxies = self._scrap_json(link)
            except Exception as e:
                raise e
        return list(self._proxies)

if __name__ == "__main__":
    provider = RemoteProvider()
    sites = provider.get_target_sites()