# modelBomb.py


class ModelBomb:

    id = 1

    def __init__(self, s_power, s_timer, path):
        self.__id = ModelBomb.id
        ModelBomb.id += 1
        self.__s_power = s_power
        self.__s_timer = s_timer
        self.__path = path

    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_s_power(self):
        return self.__s_power

    def get_s_timer(self):
        return self.__s_timer

    def get_path(self):
        return self.__path

    def set_s_power(self, s_power):
        self.__s_power = s_power

    def set_s_timer(self, s_timer):
        self.__s_timer = s_timer

    def set_path(self, path):
        self.__path = path