import psutil
import operator
import psutil
from PyQt5.QtWidgets import QMainWindow
from ui.main import Ui_MainWindow
from api import basicInfo


class mainUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.setupUi(self)
        basicInfo.getInfo()
        self.label_id.setText(basicInfo.g_summoner_name)
        self.label_id.repaint()
        self.label_uuid.setText(basicInfo.g_summoner_puuid)
        self.label_uuid.repaint()
