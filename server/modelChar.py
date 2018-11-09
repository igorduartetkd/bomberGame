#modelChar.py


class ModelChar:
    id = 1

    def __init__(self, s_id_bomb_model, s_speed, s_n_bomb_max, s_power_bomb_add, path):
        self.__id = ModelChar.id
        ModelChar.id += 1
        self.__s_id_bomb_model = s_id_bomb_model
        self.__s_speed = s_speed
        self.__s_n_bomb_max = s_n_bomb_max
        self.__s_power_bomb_add = s_power_bomb_add
        self.__path = path

    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_s_id_bomb_model(self):
        return self.__s_id_bomb_model

    def get_s_speed(self):
        return self.__s_speed

    def get_s_n_bomb_max(self):
        return self.__s_n_bomb_max

    def get_s_power_bomb_add(self):
        return self.__s_power_bomb_add

    def get_path(self):
        return self.__path

    def set_s_id_bomb_model(self, s_id_bomb_model):
        self.__s_id_bomb_model = s_id_bomb_model

    def set_s_speed(self, s_speed):
        self.__s_speed = s_speed

    def set_s_n_bomb_max(self, s_n_bomb_max):
        self.__s_n_bomb_max = s_n_bomb_max

    def set_s_power_bomb_add(self, s_power_bomb_add):
        self.__s_power_bomb_add = s_power_bomb_add

    def set_path(self, path):
        self.__path = path
