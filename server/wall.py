# wall.py
from server.element import Element


class Wall(Element):
    id = 0

    def __init__(self, orientation, position, id_model, scale, alpha, id_gift):
        super().__init__(orientation, position, id_model,scale,alpha)
        self.__id = Wall.id
        Wall.id += 1
        self.__id_gift = id_gift

    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_id_gift(self):
        return self.__id_gift

    def set_id_gift(self, id_gift):
        self.__id_gift = id_gift

    # PUBLIC METHODS
    def surprise(self):
        if self.get_id_gift() == 0:
            return False
        return True
