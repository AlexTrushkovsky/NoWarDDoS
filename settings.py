VERSION = 7
SITES_HOSTS = ["https://raw.githubusercontent.com/opengs/uashieldtargets/master/sites.json"]
PROXIES_HOSTS = ["https://raw.githubusercontent.com/opengs/uashieldtargets/master/proxy.json"]
MAX_REQUESTS_TO_SITE = 200
DEFAULT_THREADS = 500
TARGET_UPDATE_RATE = 600
READ_TIMEOUT = 10
SUPPORTED_PLATFORMS = {
    'linux': 'Linux'
}
UPDATE_URL = "https://gist.githubusercontent.com/AlexTrushkovsky/041d6e2ee27472a69abcb1b2bf90ed4d/raw/nowarversion.json"
BROWSER = {'browser': 'firefox', 'platform': 'android', 'mobile': True}
