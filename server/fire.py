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
        if self.__get_current_timer() % 2:
            factor = (-1) ** int(self.__get_current_timer() / (self.__time_life/2))
            x, y = self.get_scale()
            self.set_scale([x + factor, y + factor])
            alpha = self.get_alpha()
            self.set_alpha(alpha + factor*10)

    # PUBLIC METHODS
    def clock(self):
        self.__set_current_timer(self.__get_current_timer() + 1)
        self.__fire_beat()

    def is_ended(self):
        if self.__time_life <= self.__current_timer:
            return True
        return False

    def check_collision(self, element):
        xs, ys = self.get_position()
        xs = round(xs / 53) * 53 + 10
        ys = round(ys / 53) * 53 + 10
        x = [[0, 0], [0, 0]]
        y = [[0, 0], [0, 0]]
        x[0][0], y[0][0] = [xs, ys]
        x[1][0], y[1][0] = element.get_position()

        x_scale1, y_scale1 = self.get_scale()
        x_scale2, y_scale2 = element.get_scale()
        x[0][1] = x[0][0] + x_scale1 -30
        x[1][1] = x[1][0] + x_scale2
        y[0][1] = y[0][0] + y_scale1 -30
        y[1][1] = y[1][0] + y_scale2

        if x[0][0] >= x[1][1] or x[0][1] <= x[1][0] or y[0][0] >= y[1][1] or y[0][1] <= y[1][0]:
            return False

        return True
