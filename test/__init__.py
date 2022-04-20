from lcu_driver import Connector

connector = Connector()


@connector.ready
async def connect(connection):
    print(connection.address)
    print('LCU API is ready to be used.')


@connector.close
async def disconnect(connection):
    print('The client was closed')
    await connector.stop()


@connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
async def icon_changed(connection, event):
    print(event.data)
