import psutil
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMessageBox

from exec.mainLogic import mainUI


def CheckProcess():
    process = psutil.pids()
    for pid in process:
        if psutil.Process(pid).name() == 'LeagueClient.exe':
            return pid
    else:
        return None


class warning(QWidget):
    def __init__(self):
        super(warning, self).__init__()  # 1
        QMessageBox.warning(self, '未检测到客户端!', '请先启动客户端再启动本程序!',
                                  QMessageBox.Ok)


if __name__ == '__main__':
    if CheckProcess() is None:
        app = QApplication(sys.argv)
        warning1 = warning()
        sys.exit(app.exec_())
    else:
        app = QApplication(sys.argv)
        ui = mainUI()
        ui.show()
        sys.exit(app.exec_())
