import base64
import os

import requests
import util.analysisUtils
from PIL import Image
from PyQt5.QtCore import QThread

auth_key1 = '-'
port1 = '-'
my_puuid = '-'
my_profileIconId = '-'
g_ranked_solo = '-'
g_ranked_flex = '-'
g_icon_path = '-'

def initial(auth_key, port, puuid, profileIconId):
    global auth_key1, port1, my_puuid, my_profileIconId
    auth_key1 = auth_key
    port1 = port
    my_puuid = puuid
    my_profileIconId = str(profileIconId)


class Thread_2(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        data_bytes = ("riot:" + auth_key1).encode()
        auth = bytes.decode(base64.b64encode(data_bytes))
        port = port1
        headers = {'User-Agent': 'LeagueOfLegendsClient',
                   'authorization': 'Basic' + ' ' + auth}

        def get_ranked_info():
            response = requests.get('https://127.0.0.1:' + port + '/lol-ranked/v1/ranked-stats/' + my_puuid,
                                    headers=headers,
                                    verify=False)
            response_json = response.json()

            solo_tier = response_json['queueMap']['RANKED_SOLO_5x5']['tier']
            solo_division = response_json['queueMap']['RANKED_SOLO_5x5']['division']
            solo_point = response_json['queueMap']['RANKED_SOLO_5x5']['leaguePoints']
            flex_tier = response_json['queueMap']['RANKED_FLEX_SR']['tier']
            flex_division = response_json['queueMap']['RANKED_FLEX_SR']['division']
            flex_point = response_json['queueMap']['RANKED_FLEX_SR']['leaguePoints']
            if solo_tier != 'NONE':
                global g_ranked_solo
                g_ranked_solo = util.analysisUtils.tier_analysis(solo_tier, solo_division, solo_point)
            else:
                g_ranked_solo = "无段位"

            if flex_tier != 'NONE':
                global g_ranked_flex
                g_ranked_flex = util.analysisUtils.tier_analysis(flex_tier, flex_division, flex_point)
            else:
                g_ranked_flex = "无段位"

        def get_profileIconId():
            response = requests.get(
                'https://127.0.0.1:' + port + '/lol-game-data/assets/v1/profile-icons/' + my_profileIconId + '.jpg',
                headers=headers,
                verify=False)
            path = os.path.dirname(os.getcwd())
            if not os.path.exists(path + "/tmp/images"):
                os.makedirs(path + '/tmp/images')
            picname = path + "/tmp/images/" + "profileIcon_" + my_profileIconId + ".png"
            with open(picname, 'wb') as f:
                f.write(response.content)
            global g_icon_path
            g_icon_path = picname

        get_ranked_info()
        get_profileIconId()
        global g_ranked_solo, g_ranked_flex
        print(g_ranked_solo)
        print(g_ranked_flex)
