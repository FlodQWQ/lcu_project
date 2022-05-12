import json

from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("../webdriver/chromedriver.exe", chrome_options=options)
password = '-'
port = '-'


def initial(password1, port1):
    global password, port
    password = password1
    port = port1


def get(order):
    driver.get('https://riot:' + password + '@127.0.0.1:' + port + order)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ss = soup.select('pre')[0]
    res = json.loads(ss.text)
    driver.close()
    print(res)
    return res
