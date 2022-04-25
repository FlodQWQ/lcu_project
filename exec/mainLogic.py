import threading
import time
from PyQt5.QtWidgets import QMainWindow
from ui.main import Ui_MainWindow
from api import lcu_api, clientListener


class mainUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.thread_1 = lcu_api.Thread_1()
        self.thread_1.start()
        self.setupUi(self)
        time.sleep(0.5)
        self.label_id.setText(lcu_api.g_summoner_name)
        self.label_id.repaint()
        self.label_uuid.setText(lcu_api.g_summoner_puuid)
        self.label_uuid.repaint()


class myThread_status(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        mainUI.listen_status()
