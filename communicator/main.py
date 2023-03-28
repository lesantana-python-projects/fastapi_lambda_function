from mangum import Mangum
from communicator import views
from communicator.server import ServerCommunicator


def main():
    server = ServerCommunicator()
    return server.start(views)


app = main()
handler = Mangum(app, lifespan="off")
