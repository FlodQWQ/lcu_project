from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from util import okhttpUtils,webdriverUtils


class Thread_3(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        def get_player_info(summonerId):

        def teammate_info():
            room = webdriverUtils.get('/lol-champ-select/v1/session')
            players_teammate = list()
            for player in room['myTeam']:
                players_teammate.append(get_player_info(str(player['summonerId'])))
            for player in players_teammate:
                okhttpUtils.get_match_history(player, 20)

        teammate_info()