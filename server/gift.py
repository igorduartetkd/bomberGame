# gift.py
from element import Element


class Gift(Element):
    id = 0

    def __init__(self, orientation, position, id_model, scale, alpha, more_speed, more_n_bombs, more_power):
        super().__init__(orientation, position, id_model, scale, alpha)
        id = Gift.id
        Gift.id += 1
        self.__more_speed = more_speed
        self.__more_n_bombs = more_n_bombs
        self.__more_power = more_power

    # GETTERS AND SETTERS
    def get_more_speed(self):
        return self.__more_speed

    def get_more_n_bombs(self):
        return self.__more_n_bombs

    def get_more_power(self):
        return self.__more_power

    def set_more_speed(self, more_speed):
        self.__more_speed = more_speed

    def set_more_n_bombs(self, more_n_bombs):
        self.__more_n_bombs = more_n_bombs

    def set_more_power(self, more_power):
        self.__more_power = more_power

