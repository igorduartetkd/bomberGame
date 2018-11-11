#modelGift.py


class ModelGift:

    id = 1

    def __init__(self, s_more_speed, s_more_n_bombs, s_more_power, path):
        self.__id = ModelGift.id
        ModelGift.id += 1
        self.__s_more_speed = s_more_speed
        self.__s_more_n_bombs = s_more_n_bombs
        self.__s_more_power = s_more_power
        self.__path = path

    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_s_more_speed(self):
        return self.__s_more_speed

    def get_s_more_n_bombs(self):
        return self.__s_more_n_bombs

    def get_s_more_power(self):
        return self.__s_more_power

    def get_path(self):
        return self.__path

    def set_s_more_speed(self, s_more_speed):
        self.__s_more_speed = s_more_speed

    def set_s_more_n_bombs(self, s_more_n_bombs):
        self.__s_more_n_bombs = s_more_n_bombs

    def set_s_more_power(self, s_more_power):
        self.__s_more_power = s_more_power

    def set_path(self, path):
        self.__path = path
