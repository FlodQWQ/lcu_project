from lcu_driver import Connector

connector = Connector()


@connector.ws.register('/lol-gameflow/v1/gameflow-phase', event_types=('UPDATE',))
async def client_status_changed(connection, event):
    print(event.data)


connector.start()
