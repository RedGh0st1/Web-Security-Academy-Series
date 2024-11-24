import requests
import sys
import urllib3
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)