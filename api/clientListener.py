# import threading
# import time
# from api.api import connector
#
#
# g_client_status = "-"
#
#
# class myThread1(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         getInfo()
#
#
#
#
#
# def getInfo():
#     while 1:
#         @connector.ready
#         async def connect(connection):
#             await client_status_changed(connection)
#         time.sleep(0.5)
#
#
# def runTread():
#     thread2 = myThread("Thread-2")
#     thread2.start()
#     thread2.join()
