#server.py
import Pyro4
from modelChar import ModelChar

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Server(object):
    def __init__(self):
        self.__bombs = {}
        self.__chars = {}
        self.__walls = {}
        self.__gifts = {}

        self.__load_models()

    @staticmethod
    def read_model_char():
        model_chars_return = {}
        file_descriptor = open("modelsDescriptor/charDesc.txt", 'r')
        lines = file_descriptor.readlines()
        file_descriptor.close()
        columns = int(lines.pop(0).split()[1])
        lines.pop(0)
        print(columns)
        for line in lines:
            if len(line.split()) == columns:
                s_id_bomb_model, s_speed, s_n_bomb_max, s_power_bomb_add = map(int, line.split()[:-1])
                path = line.split()[-1:][0]
                model_char = ModelChar(s_id_bomb_model, s_speed, s_n_bomb_max, s_power_bomb_add, path)
                model_chars_return[model_char.get_id()] = model_char
        return model_chars_return
    # TODO IMPLEMENTAR READMODELBOMB READMODELGIFT READMODELWALL AGUARDANDO CLASSES

    # PRIVATE METHODS
    def __load_models(self):
        self.__chars = Server.read_model_char()

    def __create_random_walls(self):
        random_walls_return = {}



def main():
    server = Server()
    daemon = Pyro4.Daemon()
    uri = daemon.register(server)
    ns = Pyro4.locateNS()
    ns.register("server.bombergame", uri)
    daemon.requestLoop()


if __name__=="__main__":
    main()
