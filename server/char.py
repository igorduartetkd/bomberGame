# char.py
from element import Element
import math


class Char(Element):
    id = 1

    def __init__(self, orientation, position, id_model, scale, alpha, nick, id_bomb_model, speed, n_bomb_max=1,
                 power_bomb_add=0):
        super().__init__(orientation, position, id_model, scale, alpha)
        self.__id = Char.id
        Char.id += 1
        self.__nick = nick
        self.__id_bomb_model = id_bomb_model
        self.__speed = speed
        self.__n_bomb_max = n_bomb_max
        self.__n_bomb_implanted = 0
        self.__power_bomb_add = power_bomb_add


    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_nick(self):
        return self.__nick

    def get_id_bomb_model(self):
        return self.__id_bomb_model

    def get_speed(self):
        return self.__speed

    def get_n_bomb_max(self):
        return self.__n_bomb_max

    def get_power_bomb_add(self):
        return self.__power_bomb_add

    def get_n_bomb_implanted(self):
        return self.__n_bomb_implanted

    def set_nick(self, nick):
        self.__nick = nick

    def set_id_bomb_model(self, id_bomb_model):
        self.__id_bomb_model = id_bomb_model

    def set_speed(self, speed):
        self.__speed = speed

    def set_n_bomb_max(self, n_bomb_max):
        self.__n_bomb_max = n_bomb_max

    def set_power_bomb_add(self, power_bomb_add):
        self.__power_bomb_add = power_bomb_add

    def set_n_bomb_implanted(self, n_bomb_implanted):
        self.__n_bomb_implanted = n_bomb_implanted

    # PUBLIC METHODS
    def move(self, direction):
        super().set_orientation(direction)
        # right = 0; up = 90; left = 180; down = 270
        x = self.get_speed() * math.cos(direction)
        y = self.get_speed() * math.sin(direction)
        movement = [x, y]
        super()._change_position(movement)

    def put_bomb(self):
        if self.get_n_bomb_implanted() >= self.get_n_bomb_max():
            return False
        self.set_n_bomb_implanted(self.get_n_bomb_implanted() + 1)
        return True

    def bomb_exploded(self):
        self.set_n_bomb_implanted(self.get_n_bomb_implanted() - 1)

# unit tests
