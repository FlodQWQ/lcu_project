import json

from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("../webdriver/chromedriver.exe", chrome_options=options)


def get(password, port, order):
    res = webdriver.request('GET', 'https://riot:X7aZdOdVzi9HBgejAdNr2A@127.0.0.1:5254/lol-champ-select/v1/session')
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ss = soup.select('pre')[0]
    res = json.loads(ss.text)
    driver.close()
    print(res)
    return res

