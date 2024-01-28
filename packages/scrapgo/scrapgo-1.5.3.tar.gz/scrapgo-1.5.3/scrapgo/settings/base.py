import os
from datetime import timedelta

from requests_cache import DO_NOT_CACHE, NEVER_EXPIRE, EXPIRE_IMMEDIATELY

# Request
# USER_AGENT_NAME = 'chrome'
REQUEST_DELAY = 0.5, 1.5
RETRY_INTERVAL_SECONDS = 10, 15, 20
ALLOWABLE_ERROR_STATUS_CODES = []
REQUEST_MAX_WORKERS = 50

REQUEST_LOGGING = True

# FAKE_USER_AGENT
FAKE_USER_AGENT_USE_CACHE_SERVER = True
FAKE_USER_AGENT_AGENT_NAME = 'chrome'


# Request Cache
REQUEST_CACHE_CACHE_NAME = 'scrapgo.sqlite'
REQUEST_CACHE_BACKEND = os.environ.get('REQUEST_CACHE_BACKEND', 'sqlite')
REQUEST_CACHE_EXPIRE_AFTER = NEVER_EXPIRE
REQUEST_CACHE_ALLOWABLE_METHODS = 'GET', 'POST',
REQUEST_CACHE_ALLOWABLE_CODES = 200,
REQUEST_CACHE_OLD_DATA_ON_ERROR = False
REQUEST_CACHE_CACHE_CONTROL = False

# requests
REQUESTS_TIMEOUT = 45
REQUESTS_PROXY = None

# SoupParser
CRAWL_TARGET_ATTRS = ['href', 'src',]
PARSE_CONTENT_TYPES = [
    'text/css', 'text/html', 'text/javascript', 'text/plain', 'text/xml',
    'application/json'
]

BS4_FEATURES = 'html.parser'
BS4_PARSE_ONLY = None
BS4_FROM_ENCODING = 'utf-8'
BS4_EXCLUDE_ENCODINGS = None
BS4_ELEMENT_CLASSES = None


EXTRACT_AUTO_STRIP = True
EXTRACT_AUTO_SOUP2TEXT = True
EXTRACT_AUTO_PRETTIFY = True

CRAWL_SUSPENDE_LOOP_POLLING_RATE = 1


CHROME_BROWSER_OPTIONS = [
    # 'headless',
]
CHROME_BROWSER_EXPERIMENTAL_OPTIONS = {'detach': True}
CHROME_BROWSER_SETTINGS = {
    'set_window_position': (100, 100),
    'set_window_size': (1200, 1000)
}