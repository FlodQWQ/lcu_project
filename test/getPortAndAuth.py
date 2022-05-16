from lcu_driver import Connector

connector = Connector()


async def getInfo(connection):
    port = connection.port
    auth_key = connection.auth_key
    print(port)
    print(auth_key)


@connector.ready
async def connect(connection):
    await getInfo(connection)

connector.start()
