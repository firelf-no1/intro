############################################################
# Helper class
############################################################


class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
     NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
     implementations are for you to carry out.
    """
    UP = 'W'
    DOWN = 'S'
    LEFT = 'A'
    RIGHT = 'D'

    NOT_MOVING = 'T'

    VERTICAL = 0
    HORIZONTAL = 1

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)






############################################################
# Class definition
############################################################


class Car:
    """
    A class representing a car in rush hour game.
    A car is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A car drives on its vertical\horizontal axis back and
    forth until reaching the board's boarders. A car can only drive to an empty
    slot (it can't override another car).
    """

    def __init__(self, color, length, location, orientation):
        """
        A constructor for a Car object
        :param color: A string representing the car's color
        :param length: An int in the range of (2,4) representing the car's
         length.
        :param location: A tuple representing the car's head (x, y) location
        :param orientation: An int representing the car's orientation
        """
        self.color = color
        self.length = length
        self._location = location
        self.orientation = orientation
