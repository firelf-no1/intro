from screen import Screen
from ship import Ship
import random
import math


SIZE_FACTOR = 10
NORMALIZATION_FACTOR = -5
ASTEROIDS_SIZES = 3


class Asteroid():
    """
    The asteroid class for the game asteroids
    """
    def __init__(self, ship):
        """
        :param ship: takes the parameters of the object ship
        :initializing: the parameters of the asteroid
        """
        self.lx = random.random() * (Screen.SCREEN_MAX_X -
                                     Screen.SCREEN_MIN_X) + Screen.SCREEN_MIN_X
        self.ly = random.random() * (Screen.SCREEN_MAX_Y -
                                     Screen.SCREEN_MIN_Y) + Screen.SCREEN_MIN_Y
        while self.lx == ship.get_lx() and self.ly == ship.get_ly():
            self.lx = random.random() * (Screen.SCREEN_MAX_X -
                                         Screen.SCREEN_MIN_X) + \
                      Screen.SCREEN_MIN_X
            self.ly = random.random() * (Screen.SCREEN_MAX_Y -
                                         Screen.SCREEN_MIN_Y) + \
                      Screen.SCREEN_MIN_Y
        self.dx = random.random() * 6 - 3
        self.dy = random.random() * 6 - 3
        self.size = ASTEROIDS_SIZES

    def get_lx(self):
        """
        :return: the location of the asteroid on the x axis
        """
        return self.lx

    def get_ly(self):
        """
        :return: the location of the asteroid on the y axis
        """
        return self.ly

    def set_lx(self, n_lx):
        """
        :param n_lx: the new location of the asteroid on the x axis
        :return: updates the location of the asteroid on the x axis
        """
        self.lx = n_lx

    def set_ly(self, n_ly):
        """
        :param n_ly: the new location of the asteroid on the y axis
        :return: updates the location of the asteroid on the y axis
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
        :param n_dx: the new speed of the asteroid on the x axis
        :return: update the speed of the asteroid  on the x axis
        """
        self.dx = n_dx

    def set_dy(self, n_dy):
        """
        :param n_dy: the new speed of the asteroid on the y axis
        :return: update the speed of the asteroid  on the y axis
        """
        self.dy = n_dy

    def get_size(self):
        """
        :return: the asteroid size
        """
        return self.size

    def set_size(self, n_size):
        """
        :param n_size: the new size of the asteroid
        :return: update the size of the asteroid
        """
        self.size = n_size

    def get_radius(self):
        """
        :return: the asteroid radius
        """
        r = (self.get_size() * SIZE_FACTOR + NORMALIZATION_FACTOR)
        return r

    def has_intersection(self, obj):
        """
        :param obj: an object that we want to check if it collided with an
        asteroid
        :return: if there was a collision true else false
        """
        x = ((obj.get_lx() - self.get_lx()) ** 2)
        y = ((obj.get_ly() - self.get_ly()) ** 2)
        distance = int(math.sqrt(x + y))
        radius1 = obj.get_radius()
        radius2 = self.get_radius()
        if distance <= (radius2 + radius1):
            return True
        elif distance > (radius2 + radius1):
            return False

    def set_hit_speed(self, factor, torpedo, asteroid):
        """
        :param factor: the speed parameter of the asteroid
        :param torpedo: the torpedo that hit the asteroid
        :param asteroid: the asteroid the torpedo hit
        :return: update the new asteroid new coordinate
        """
        self.set_dx(((torpedo.get_dx() + factor * asteroid.get_dx()) /
                     math.sqrt((asteroid.get_dx() ** 2) +
                               (asteroid.get_dy() ** 2))))
        self.set_dy(((torpedo.get_dy() + factor * asteroid.get_dy()) /
                     math.sqrt((asteroid.get_dx() ** 2) +
                               (asteroid.get_dy() ** 2))))

