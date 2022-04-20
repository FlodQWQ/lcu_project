import operator
import threading
from lcu_driver import Connector

connector = Connector()

g_summoner_name = '-'
g_summoner_puuid = '-'
g_game_zone = '-'


async def get_summoner_data(connection):
    summoner = await connection.request('GET', '/lol-summoner/v1/current-summoner')
    summoner_data = await summoner.json()
    global g_summoner_name, g_summoner_puuid
    g_summoner_name = summoner_data['displayName']
    g_summoner_puuid = summoner_data['puuid']


async def get_game_zone(connection):
    environment = await connection.request('GET', '/riotclient/v1/crash-reporting/environment')
    game_zone_data = await environment.json()
    HN = ["艾欧尼亚", "祖安", "诺克萨斯", "班德尔城", "皮尔特沃夫", "战争学院", "巨神峰", "雷瑟守备", "裁决之地", "黑色玫瑰", "暗影岛", "钢铁烈阳", "水晶之痕",
          "均衡教派",
          "影流", "守望之海", "征服之海", "卡拉曼达", "皮城警备"]
    WT = ["比尔吉沃特", "德玛西亚", "弗雷尔卓德", "无畏先锋", "恕瑞玛", "扭曲丛林", "巨龙之巢"]
    EDU = ["教育网"]
    BGP = ["男爵领域", "峡谷之巅"]
    if operator.contains(game_zone_data['environment'], 'HN'):
        list_str = list(game_zone_data['environment'])
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = HN[game_zone_num - 1]
    elif operator.contains(game_zone_data['environment'], 'WT'):
        list_str = list(game_zone_data['environment'])
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = WT[game_zone_num - 1]
    elif operator.contains(game_zone_data['environment'], 'EDU'):
        list_str = list(game_zone_data['environment'])
        list_str.pop(0)
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = EDU[game_zone_num - 1]
    else:
        list_str = list(game_zone_data['environment'])
        list_str.pop(0)
        list_str.pop(0)
        list_str.pop(0)
        game_zone_num = int(''.join(list_str))
        game_zone = BGP[game_zone_num - 1]
    global g_game_zone
    g_game_zone = game_zone


class info(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        getInfo()


def getInfo():
    @connector.ready
    async def connect(connection):
        await get_summoner_data(connection)
        await get_game_zone(connection)

    connector.start()


def runTread():
    thread1 = info("Thread-1")
    thread1.start()
    thread1.join()
