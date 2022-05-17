import base64
import json

from lcu_driver import Connector

connector = Connector()


async def getInfo(connection):
    port = connection.port
    auth_key = connection.auth_key
    print(port)
    print(auth_key)
    data_bytes = ("riot:" + auth_key).encode()
    auth = bytes.decode(base64.b64encode(data_bytes))
    print(auth)

@connector.ready
async def connect(connection):
    await getInfo(connection)

connector.start()
