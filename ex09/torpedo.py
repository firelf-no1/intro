import math

ACCELERATION_FACTOR = 2
TORPEDO_RADIUS = 4


class Torpedo():
    """
    The torpedo class for the game asteroids
    """
    def __init__(self, ship):
        """
        :param ship: takes the parameters of the object ship
        :initializing: the parameters of the torpedo
        """
        self.lx = ship.get_lx()
        self.ly = ship.get_ly()
        self.dx = ship.get_dx()
        self.dy = ship.get_dy()
        self.life_span = 200
        self.heading = ship.get_heading()

    def get_heading(self):
        """
        :return: the heading of the torpedo
        """
        return self.heading

    def get_lx(self):
        """
        :return: the location of the torpedo on the x axis
        """
        return self.lx

    def get_ly(self):
        """
        :return: the location of the torpedo on the y axis
        """
        return self.ly

    def set_lx(self, n_lx):
        """
        :param n_lx: the new location of the torpedo on the x axis
        :return: updates the location of the torpedo on the x axis
        """
        self.lx = n_lx

    def set_ly(self, n_ly):
        """
        :param n_ly: the new location of the torpedo on the y axis
        :return: updates the location of the torpedo on the y axis
        """
        self.ly = n_ly

    def get_dx(self):
        """
        :return: the speed of the torpedo on the x axis
        """
        return self.dx

    def get_dy(self):
        """
        :return: the speed of the torpedo on the y axis
        """
        return self.dy

    def set_dx(self):
        """
        :return: update the speed of the torpedo  on the x axis
        """
        self.dx = (self.dx + ACCELERATION_FACTOR *
                   math.cos(math.radians(self.get_heading())))

    def set_dy(self):
        """
        :return: update the speed of the torpedo  on the y axis
        """
        self.dy = (self.dy + ACCELERATION_FACTOR *
                   math.sin(math.radians(self.get_heading())))

    def get_radius(self):
        """
        :return: the torpedo radius
        """
        return TORPEDO_RADIUS

    def get_life(self):
        """
        :return: the amount of life the torpedo has left
        """
        return self.life_span

    def life_update(self):
        """
        :return: updated number of lifes
        """
        self.life_span -= 1
