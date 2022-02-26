import cloudscraper
import requests
import os
from bs4 import BeautifulSoup
# from ctypes import windll
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

VERSION = 0
HOSTS = ["http://46.4.63.238/api.php"]
MAX_REQUESTS = 5000
disable_warnings()
def clear(): return system('cls')
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")
threads = int(sys.argv[1])

def update():
    with open('a.txt') as f:
        a = int(f.read())
    with open('a.txt', 'w') as output:
        output.write(str(a+1))
    b = 1
    print a+b
    
def start_new():
    

if __name__ == '__main__':
    clear()
    checkReq()
    checkUpdate()
    for _ in range(threads):
        Thread(target=mainth).start()
    Thread(target=cleaner, daemon=True).start()
