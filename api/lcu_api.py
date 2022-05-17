from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from lcu_driver import Connector
from api import  lcu_requests_api
from util import webdriverUtils, analysisUtils, okhttpUtils

connector = Connector()

g_summoner_name = '-'
g_summoner_puuid = '-'
g_game_zone = '-'
g_client_status = '-'
link = '-'
auth = '-'
players_teammate = list()


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
            lcu_requests_api.initial(auth_key, port, summoner_data['puuid'], summoner_data['profileIconId'])
            okhttpUtils.init(port, auth_key)

        async def get_game_zone(connection):
            environment = await connection.request('GET', '/riotclient/v1/crash-reporting/environment')
            game_zone_data = await environment.json()
            game_zone = analysisUtils.game_zone_analysis(game_zone_data)
            global g_game_zone
            g_game_zone = game_zone

        async def get_player_info(summonerId, connection):
            player = await connection.request('GET', '/lol-summoner/v1/summoners/' + summonerId)
            player_info = await player.json()
            return player_info

        @connector.ws.register('/lol-gameflow/v1/gameflow-phase', event_types=('UPDATE',))
        async def client_status_changed(connection, event):
            status = event.data
            global g_client_status
            g_client_status = analysisUtils.client_status_analysis(status)

        @connector.ready
        async def connect(connection):
            await get_summoner_data(connection)
            await get_game_zone(connection)
            await client_status_changed(connection)

        connector.start()

