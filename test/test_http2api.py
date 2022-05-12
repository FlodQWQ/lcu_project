import re

import requests
import httpx
import asyncio
from hyper.contrib import HTTP20Adapter
from requests.auth import HTTPBasicAuth

headers = {':authority': '127.0.0.1:7455',
           ':method': 'GET',
           ':path': '/lol-champ-select/v1/session',
           ':scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'sec-fetch-dest': 'document',
           'Sec-Fetch-Site': 'none',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}

# response = requests.get('https://127.0.0.1:5500/lol-champ-select/v1/session', headers=headers, verify=False)

s = requests.Session()
s.mount('https://127.0.0.1:7455', HTTP20Adapter())
response = s.get('https://127.0.0.1:7455/lol-champ-select/v1/session',
                 auth=HTTPBasicAuth('riot', 'nEuDsNkDXqUAhiG7vTfL-A'), verify=False, headers=headers)
print(response.json())
print(response.status_code)

# async def main():
#     client = httpx.Client(http2=True, verify=False)
#     response = await client.get('https://127.0.0.1:7455/lol-summoner/v1/current-summoner', auth=HTTPBasicAuth('riot','nEuDsNkDXqUAhiG7vTfL-A'), )
#     print(response.json())
#     print(response.status_code)
#
# asyncio.run(main())
