import threading
import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from ui.main import Ui_MainWindow
from api import lcu_api, lcu_requests_api


class mainUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.thread_1 = lcu_api.Thread_1()
        self.thread_1.start()
        self.setupUi(self)
        while lcu_api.g_summoner_name == '-':
            time.sleep(0.25)
        self.thread_2 = lcu_requests_api.Thread_2()
        self.thread_2.start()
        while lcu_requests_api.g_ranked_flex == '-' or lcu_requests_api.g_icon_path == '-':
            time.sleep(0.25)
        self.init_info()
        self.set_summoner_icon()
        self.countTimer = QTimer(self)
        self.countTimer.start(500)
        self.countTimer.timeout.connect(self.refresh_ui)

    def refresh_ui(self):
        self.label_status.setText(lcu_api.g_client_status)
        self.label_status.repaint()

    def init_info(self):
        self.label_id.setText(lcu_api.g_summoner_name)
        self.label_id.repaint()
        self.label_solo_rank.setText(lcu_requests_api.g_ranked_solo)
        self.label_solo_rank.repaint()
        self.label_solo_rank.setText(lcu_requests_api.g_ranked_solo)
        self.label_solo_rank.repaint()
        self.label_flex_rank.setText(lcu_requests_api.g_ranked_flex)
        self.label_flex_rank.repaint()

    def set_summoner_icon(self):
        icon = QPixmap(lcu_requests_api.g_icon_path)
        width = icon.width()
        height = icon.height()
        if width / self.label_icon.width() >= height / self.label_icon.height():
            ratio = width / self.label_icon.width()
        else:
            ratio = height / self.label_icon.height()
        new_width = width / ratio
        new_height = height / ratio
        new_img = icon.scaled(new_width, new_height)
        self.label_icon.setPixmap(new_img)


class myThread_status(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        mainUI.listen_status()
