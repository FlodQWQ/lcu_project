import json
import os
import platform

from bs4 import BeautifulSoup
from selenium import webdriver

import api.lcu_requests_api


def get(request):
    if os.name == 'nt':
        if platform.release() == '10':
            options = webdriver.EdgeOptions()
            options.add_argument('headless')
            options.add_argument('ignore-certificate-errors')
            driver = webdriver.Edge("../webdriver/msedgedriver.exe", options=options)
            driver.get("https://riot:" + api.lcu_requests_api.auth_key1 + "@127.0.0.1:" + api.lcu_requests_api.port1 + request)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            ss = soup.select('pre')[0]
            res = json.loads(ss.text)
        return res
