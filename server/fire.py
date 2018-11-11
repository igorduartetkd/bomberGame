# fire.py

from element import Element


class Fire(Element):
    id = 1

    def __init__(self, orientation, position, id_model, scale, alpha, time_life, current_timer=0):
        super().__init__(orientation, position, id_model, scale, alpha)
        self.__id = Fire.id
        Fire.id += 1
        self.__time_life = time_life
        self.__current_timer = current_timer

    # GETTERS AND SETTERS
    def get_id(self):
        return self.__id

    def get_time_life(self):
        return self.__time_life

    def __get_current_timer(self):
        return self.__current_timer

    def set_time_life(self, timer_life):
        self.__time_life = timer_life

    def __set_current_timer(self, current_timer):
        self.__current_timer = current_timer

    def __fire_beat(self):
        # if self.__get_current_timer() % 2:
        factor = (-1) ** int(self.__get_current_timer() / (self.__time_life/2))
        x, y = self.get_scale()
        self.set_scale([x + factor, y + factor])

    # PUBLIC METHODS
    def clock(self):
        self.__set_current_timer(self.__get_current_timer() + 1)
        self.__fire_beat()

    def is_ended(self):
        if self.__time_life <= self.__current_timer:
            return True
        return False


