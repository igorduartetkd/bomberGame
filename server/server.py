#server.py
import Pyro4
from random import randint, sample
from char import Char
from bomb import Bomb
from gift import Gift
from wall import Wall
from modelChar import ModelChar
from modelWall import ModelWall


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Server(object):

    def __init__(self):
        self.__model_char = {}
        self.__model_bomb = {}
        self.__model_gift = {}
        self.__model_wall = {}

        self.__chars = {}
        self.__bombs = {}
        self.__gifts = {}
        self.__walls = {}


        self.__load_models()

    @staticmethod
    def read_model_char():
        model_chars_return = {}
        file_descriptor = open("modelsDescriptor/charDesc.txt", 'r')
        lines = file_descriptor.readlines()
        file_descriptor.close()
        columns = int(lines.pop(0).split()[1])
        lines.pop(0)
        for line in lines:
            if len(line.split()) == columns:
                s_id_bomb_model, s_speed, s_n_bomb_max, s_power_bomb_add = map(int, line.split()[:-1])
                path = line.split()[-1:][0]
                model_char = ModelChar(s_id_bomb_model, s_speed, s_n_bomb_max, s_power_bomb_add, path)
                model_chars_return[model_char.get_id()] = model_char
        return model_chars_return

    def read_model_wall():
        model_walls_return = {}
        file_descriptor = open("modelsDescriptor/wallDesc.txt", 'r')
        lines = file_descriptor.readlines()
        file_descriptor.close()
        columns = int(lines.pop(0).split()[1])
        lines.pop(0)
        for line in lines:
            if len(line.split()) == columns:
                path = line.split()[0]
                model_wall = ModelWall(path)
                model_walls_return[model_wall.get_id()] = model_wall
        return model_walls_return

    # TODO IMPLEMENTAR READMODELBOMB READMODELGIFT AGUARDANDO CLASSES

    # PRIVATE METHODS
    def __load_models(self):
        self.__model_char = Server.read_model_char()
        self.__model_wall = Server.read_model_wall()

    def __create_random_gift(self):
        id_model_gift = randint(0, len(self.__model_gift))
        return id_model_gift

    def create_random_walls(self):
        random_walls_return = {}
        reserved_spaces = [[1, 1], [1, 2], [2, 1],
                           [1, 6], [1, 7], [2, 7],
                           [12, 1], [13, 1], [13, 2],
                           [13, 6], [13, 7], [12, 7]]
        x = 1
        y = 1
        n = 0
        n_walls = 45
        while True:
            x = randint(1, 13)
            y = randint(1, 7)
            if x % 2 == 1 or y % 2 == 1:    # fixes walls
                if [x, y] not in reserved_spaces:
                    n += 1
                    reserved_spaces.append([x, y])
                    model_wall = self.__model_wall[0]
                    wall = Wall([x, y], 0, model_wall.get_id(), [54, 54], 255, self.__create_random_gift())
                    self.__walls[wall.get_id()] = wall
            if n == n_walls:
                break


def main():
    server = Server()
    server.create_random_walls()
    daemon = Pyro4.Daemon()
    uri = daemon.register(server)
    ns = Pyro4.locateNS()
    ns.register("server.bombergame", uri)
    daemon.requestLoop()


if __name__=="__main__":
    main()
