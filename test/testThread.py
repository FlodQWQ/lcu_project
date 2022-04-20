import threading
import time
from lcu_driver import Connector

exitFlag = 0

connector = Connector()

@connector.ready
async def connect(connection):
    print(connection.address)
    print('LCU API is ready to be used.')


@connector.close
async def disconnect(connection):
    print('The client was closed')
    await connector.stop()

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        print_time()
        print("退出线程：" + self.name)


def print_time():
    cnt = 0
    while 1:
        @connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
        async def icon_changed(connection, event):
            print(event.data)
        if cnt == 0:
            connector.start()
        cnt += 1
        time.sleep(0.5)


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)

# 开启新线程
thread1.start()
thread1.join()
print("退出主线程")
