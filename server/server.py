#server.py

import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Server(object):
    def __init__(self):
        bombs = {}
        chars = {}
        walls = {}
        gifts = {}





def main():
    server = Server()
    daemon = Pyro4.Daemon()
    uri = daemon.register(server)
    ns = Pyro4.locateNS()
    ns.register("server.bombergame", uri)
    daemon.requestLoop()


if __name__=="__main__":
    main()
