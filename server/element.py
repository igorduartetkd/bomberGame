# element.py
import math

class Element:

    def __init__(self, orientation, position, id_model, scale, alpha):
        self.__orientation = orientation
        self.__position = position
        self.__id_model = id_model
        self.__scale = scale
        self.__alpha = alpha

    # GETTERS AND SETTERS
    def get_orientation(self):
        return self.__orientation

    def get_position(self):
        return self.__position

    def get_id_model(self):
        return self.__id_model

    def get_scale(self):
        return self.__scale

    def get_alpha(self):
        return self.__alpha

    def set_orientation(self, orientation):
        if orientation == 90:
            orientation = 270
        elif orientation == 270:
            orientation = 90
        self.__orientation = orientation

    def set_position(self, position):
        self.__position = position

    def set_id_model(self, id_model):
        self.__id_model = id_model

    def set_scale(self, scale):
        self.__scale = scale

    def set_alpha(self, alpha):
        self.__alpha = alpha

    # PROTECTED METHODS
    def _change_position(self, movement):
        newPosition = []
        for it1, it2 in zip(movement, self.get_position()):
            newPosition.append(it1 + it2)
        self.set_position(newPosition)

    # PRIVATE METHODS
    def check_collision(self, element):
        x = [[0, 0], [0, 0]]
        y = [[0, 0], [0, 0]]
        x[0][0], y[0][0] = self.get_position()
        x[0][0] *= 1.01
        y[0][0] *= 1.01
        x[1][0], y[1][0] = element.get_position()
        x[1][0] *= 1.01
        y[1][0] *= 1.01

        x_scale1, y_scale1 = self.get_scale()
        x_scale2, y_scale2 = element.get_scale()
        x[0][1] = x[0][0] + x_scale1 * 0.99
        x[1][1] = x[1][0] + x_scale2 * 0.99
        y[0][1] = y[0][0] + y_scale1 * 0.99
        y[1][1] = y[1][0] + y_scale2 * 0.99

        if x[0][0] >= x[1][1] or x[0][1] <= x[1][0] or y[0][0] >= y[1][1] or y[0][1] <= y[1][0]:
            return False

        return True

