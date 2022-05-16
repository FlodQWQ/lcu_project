import operator
import api.lcu_special_api
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from lcu_driver import Connector
import api.htmlUtil
connector = Connector()

g_summoner_name = '-'
g_summoner_puuid = '-'
g_game_zone = '-'
g_client_status = '-'
link = '-'
auth = '-'


class Thread_1(QThread):
    def __init__(self):
        super().__init__()

    def run(self):

        async def get_summoner_data(connection):
            port = str(connection.port)
            auth_key = connection.auth_key
            summoner = await connection.request('GET', '/lol-summoner/v1/current-summoner')
            summoner_data = await summoner.json()
            global g_summoner_name, g_summoner_puuid
            g_summoner_name = summoner_data['displayName']
            g_summoner_puuid = summoner_data['puuid']
            api.htmlUtil.initial(auth_key, port, summoner_data['puuid'], summoner_data['profileIconId'])

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

        @connector.ws.register('/lol-gameflow/v1/gameflow-phase', event_types=('UPDATE',))
        async def room_info(connection, event):
            status = event.data
            if status == "ChampSelect":
                room = api.htmlUtil.get('/lol-champ-select/v1/session')
                # room_data = await room.json()
                # print(room_data)

        @connector.ws.register('/lol-gameflow/v1/gameflow-phase', event_types=('UPDATE',))
        async def client_status_changed(connection, event):
            status = event.data
            global g_client_status
            if status == "None":
                g_client_status = "大厅中"
            elif status == "Lobby":
                g_client_status = "房间中"
            elif status == "Matchmaking":
                g_client_status = "匹配中"
            elif status == "ReadyCheck":
                g_client_status = "找到对局"
            elif status == "InProgress":
                g_client_status = "游戏中"
            elif status == "WaitingForStats":
                g_client_status = "等待结算页面"
            elif status == "PreEndOfGame" or status == "PreEndOfGame":
                g_client_status = "对局结束"
            elif status == "Reconnect":
                g_client_status = "重新连接中"
            elif status == "ChampSelect":
                g_client_status = "选择英雄"
            else:
                g_client_status = "未知状态:(" + status + ")"

        @connector.ready
        async def connect(connection):
            await get_summoner_data(connection)
            await get_game_zone(connection)
            await client_status_changed(connection)

        connector.start()
