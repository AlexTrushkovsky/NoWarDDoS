import json
from typing import Optional

import cloudscraper
import cachetools.func
from random import choice
from urllib.parse import unquote
from concurrent.futures import ThreadPoolExecutor

from settings import get_settings

settings = get_settings()


def check_proxy_task(proxy: dict) -> Optional[dict]:
    scraper = cloudscraper.create_scraper(browser=settings.BROWSER)
    try:
        scraper.proxies.update({
            'http': f'http://{proxy["auth"]}@{proxy["ip"]}',
            'https': f'https://{proxy["auth"]}@{proxy["ip"]}'
        })
        scraper.get("http://httpbin.org/ip", timeout=settings.READ_TIMEOUT)
        return proxy
    except Exception:
        return None


class RemoteProvider:
    def __init__(self, targets=None):
        self.targets = [unquote(target) for target in targets] if targets else None
        self._proxies = []
        self.sites = []
        self.scraper = cloudscraper.create_scraper(browser=settings.BROWSER, )

    def _scrap_json(self, link):
        host = choice(link)
        content = self.scraper.get(host).content
        if content:
            try:
                data = json.loads(content)
                return data
            except json.decoder.JSONDecodeError:
                raise Exception('Host {} has invalid format'.format(host))
            except Exception:
                raise Exception('Unexpected error. Host {}'.format(host))
        else:
            raise Exception('Unexpected error. Host {}'.format(host))

    @cachetools.func.ttl_cache(ttl=settings.TARGET_UPDATE_RATE)
    def get_target_sites(self):
        if self.targets:
            self.sites = self.targets
        else:
            try:
                data = self._scrap_json(settings.SITES_HOSTS)
                self.sites = []
                for site in data:
                    if 'attack' not in site or ('attack' in site and not site['attack'] == 0):
                        if not site['page'].startswith('http'):
                            site['page'] = "https://" + site['page']
                        self.sites.append(unquote(site['page']))
            except Exception as e:
                raise e

        return self.sites

    @cachetools.func.ttl_cache(ttl=settings.TARGET_UPDATE_RATE)
    def get_proxies(self):
        try:
            data = self._scrap_json(settings.PROXIES_HOSTS)
            with ThreadPoolExecutor(max_workers=len(data)) as executor:
                tasks = [executor.submit(check_proxy_task, proxy) for proxy in data]
                proxies = [task.result() for task in tasks if task.result() is not None]
            self._proxies = proxies
        except Exception as e:
            raise e

        return self._proxies
