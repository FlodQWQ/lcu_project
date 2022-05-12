# import time
#
# import requests
# from hyper.contrib import HTTP20Adapter
#
#
# def h2_get(url, auth, path):
#     headers = {':authority': url,
#                ':method': 'GET',
#                ':path': path,
#                ':scheme': 'https',
#                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#                'accept-encoding': 'gzip, deflate, br',
#                'accept-language': 'zh-CN,zh;q=0.9;q=0.8',
#                'Sec-Fetch-Mode': 'navigate',
#                'Sec-Fetch-Site': 'none',
#                'Sec-Fetch-User': '?1',
#                'Upgrade-Insecure-Requests': '1',
#                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
#
#     sessions = requests.session()
#     sessions.mount('url', HTTP20Adapter())
#     response = sessions.get(url=url, auth=('riot', auth), headers=headers,)
#     print(response.json())
