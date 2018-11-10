#modelWall.py


class ModelWall:
    id = 1

    def __init__(self, path):
        self.__id = ModelWall.id
        ModelWall.id += 1
        self.__path = path

    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_path(self):
        return self.__path

    def set_path(self, path):
        self.__path = path
