import threading
import time
from lcu_driver import Connector

connector = Connector()

g_client_status = "-"


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        client_status()


def client_status():
    cnt = 0
    while 1:
        @connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
        async def icon_changed(connection, event):
            print(event.data)
        if cnt == 0:
            connector.start()
        cnt += 1
        time.sleep(0.5)
