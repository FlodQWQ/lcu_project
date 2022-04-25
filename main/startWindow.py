import psutil
import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMessageBox

from exec.mainLogic import mainUI


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        showWindow()


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


def showWindow():
    if CheckProcess() is None:
        app = QApplication(sys.argv)
        warning()
        sys.exit(app.exec_())
    else:
        app = QApplication(sys.argv)
        ui = mainUI()
        ui.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    thread_main = myThread("Thread-main")
    thread_main.start()
    thread_main.join(0.5)
