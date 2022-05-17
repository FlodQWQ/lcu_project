# import json
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
#
# options = webdriver.EdgeOptions()
# options.add_argument('headless')
# options.add_argument('ignore-certificate-errors')
#
#
# driver = webdriver.Edge("../webdriver/msedgedriver.exe", options=options)
# driver.get("https://riot:dXKL1VvCDsaddWYkue_9DA@127.0.0.1:6477/lol-champ-select/v1/session")
# html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')
# ss = soup.select('pre')[0]
# res = json.loads(ss.text)
# print(res)
# driver.close()