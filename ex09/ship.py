import math
from screen import Screen
import random

TURNING_LEFT = 7
TURNING_RIGHT = -7
SHIP_RADIUS = 1
SHIP_MAX_SPEED = 10


class Ship:
    """
    The ship class for the game asteroids
    """
    def __init__(self):
        """
        :initializing: the parameters of the ship
        """
        self.lx = random.randint(Screen.SCREEN_MIN_X,
                                 Screen.SCREEN_MAX_X)
        self.ly = random.randint(Screen.SCREEN_MIN_Y,
                                 Screen.SCREEN_MAX_Y)
        self.dx = 0
        self.dy = 0
        self.max_life = 3
        self.heading = 0

    def get_lx(self):
        """
        :return: the location of the ship on the x axis
        """
        return self.lx

    def get_ly(self):
        """
        :return: the location of the ship on the y axis
        """
        return self.ly

    def set_lx(self, n_lx):
        """
        :param n_lx: the new location of the ship on the x axis
        :return: updates the location of the ship on the x axis
        """
        self.lx = n_lx

    def set_ly(self, n_ly):
        """
        :param n_ly: the new location of the ship on the y axis
        :return: updates the location of the ship on the y axis
        """
        self.ly = n_ly

    def get_dx(self):
        """
        :return: the speed on the x axis
        """
        return self.dx

    def get_dy(self):
        """
        :return: the speed on the y axis
        """
        return self.dy

    def set_dx(self, n_dx):
        """
        :param n_dx: the new speed of the ship on the x axis
        :return: update the speed of the ship  on the x axis
        """
        self.dx = n_dx

    def set_dy(self, n_dy):
        """
        :param n_dy: the new speed of the ship on the y axis
        :return: update the speed of the ship  on the y axis
        """
        self.dy = n_dy

    def get_radius(self):
        """
        :return: the ship radius
        """
        return SHIP_RADIUS

    def get_life(self):
        """
        :return: the amount of life the ship has left
        """
        return self.max_life

    def life_update(self):
        """
        :return: updated number of lifes
        """
        self.max_life -= 1

    def turn(self, t):
        """
        :param t: the magic number that the ship has to turn
        :return: the new heading of the ship in degrees
        """
        self.heading += t
        self.heading %= 360

    def get_heading(self):
        """
        :return: the heading of the ship
        """
        return self.heading

    def fire_engine(self):
        """
        :return: update the ships speed
        """
        angle = self.heading
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        if self.dx + x <= SHIP_MAX_SPEED:
            self.set_dx(self.dx + x)
        if self.dy + y <= SHIP_MAX_SPEED:
            self.set_dy(self.dy + y)

