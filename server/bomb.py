# bomb.py

from element import Element


class Bomb(Element):
    id = 1

    def __init__(self, orientation, position, id_model, scale, alpha, id_char, power, timer):
        super().__init__(orientation, position, id_model, scale, alpha)
        self.__id = Bomb.id
        Bomb.id += 1
        self.__id_char = id_char
        self.__power = power
        self.__timer = timer
        self.__current_timer = 0

    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_id_char(self):
        return self.__id_char

    def get_power(self):
        return self.__power

    def get_timer(self):
        return self.__timer

    def __get_current_timer(self):
        return self.__current_timer

    def set_id_char(self, id_char):
        self.__id_char = id_char

    def set_power(self, power):
        self.__power = power

    def set_timer(self, timer):
        self.__timer = timer

    def __set_current_timer(self, current_timer):
        self.__current_timer = current_timer

    # PUBLIC METHODS
    def bomb_clock(self):
        self.__set_current_timer(self.__get_current_timer() + 1)

    def exploded(self):
        if self.__get_current_timer() >= self.get_timer():
            return True
        return False
