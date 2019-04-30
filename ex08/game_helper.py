############################################################
# Imports
############################################################
from car import Direction
import re

############################################################
# Constants
############################################################
#
#

VALID_COLORS = {'y', 'b', 'o', 'g', 'p', 'w', 'R'}
ERROR_CAR_COLOR = 'Not a valid car color. please try again'
ERROR_CAR_LEN = 'Not a valid car length'
ERROR_WRONG_INPUT_FORMAT = 'Wrong input format - input should be two numbers ' \
    'separated by comma, e.g. "1, 4"'
ERROR_CAR_ORN = 'Not a valid car orientation'
ERROR_COORDINATE_OUT_OF_BOUND = 'Coordinate out of bound - min ' \
    'value is: 0, max value is: '
ERROR_DIRECTION = 'Not a valid choice of direction. try again'
ERROR_NUM_CARS = 'Not a valid number of cars. try again'

MESSAGE_GET_N_CARS_INPUT = 'Insert number of cars that you want to add to the board (1 - 5): '
MESSAGE_GET_COLOR_INPUT = 'Insert a color of car to add to board. available colors are: '
MESSAGE_GET_LENGTH_INPUT = 'Insert a car length (2, 3 or 4): '
MESSAGE_GET_LOCATION_INPUT = 'Insert x,y coordinates of car location: '
MESSAGE_GET_ORIENTATION_INPUT = 'Insert car orientation (0 - vertical, 1 - horizontal): '
DIRECTIONS = '(up = ' + str(Direction.UP) + ', down = ' + str(Direction.DOWN) + \
    ' right = ' + str(Direction.RIGHT) + ', left = ' + str(Direction.LEFT) + ')'
MESSAGE_GET_DIRECTION_INPUT = 'Insert the direction you would like to move the car. ' + DIRECTIONS
MESSAGE_GAME_OVER = 'Congratulations! you released the red car!'

############################################################
# Helper functions
############################################################

def report(s):
    """
    Report a message to the user.
    :param s: A string that should be reported to the user.
    :return: None
    """
    print(s)


def get_num_cars():
    """
    The function asks the user for input of the desired number of cars to assign to the board. An valid input is an int
    in ragne (1,5) and if the inputs is not valid, the function automatically asks the user
    for an additional input until a valid input is entered.
    :return: number of cars to assign to the board (int)
    """
    pattern = re.compile('1|2|3|4|5')
    valid_input = False
    while not valid_input:
        n_cars_input = input(MESSAGE_GET_N_CARS_INPUT)
        while not pattern.match(n_cars_input):
            report(ERROR_NUM_CARS)
            n_cars_input = input(MESSAGE_GET_N_CARS_INPUT)
        valid_input = True
    return int(n_cars_input)


def get_car_input(board_size):
    """
    The function asks the user for input for initializing a car. The function
    asks for the following parameters:
    1. color of car - string
    2. length of car - int in range of (2,4)
    3. location of car a - tuple of (x, y)) representing the requested coordinate.
    4. orientation of car - int in range of (0,1)
    and returns a touple containing the given parameters.
    If one of the inputs is not valid, the function automatically asks the user
    for additional inputs until valid inputs are entered.
    :return: A tuple of the input parameters (string, int, touple, int).
    """
    def get_color_input():
        available_colors = ''.join(str(col) for col in (','.join(str(col)
                                            for col in VALID_COLORS)))
        color_input = input(MESSAGE_GET_COLOR_INPUT + available_colors)
        while not color_input in VALID_COLORS:
            report(ERROR_CAR_COLOR)
            color_input = input(MESSAGE_GET_COLOR_INPUT + available_colors)
        return color_input

    def get_length_input():
        # The following regex is designed to test the validity of the input.
        # A valid input includes two numbers separated by a comma. To be more
        # permissive, the regex allows any number of preceding, trailing or
        # between numbers inclusion of spaces.
        # for more information on regex see :
        # https://docs.python.org/3.4/library/re.html
        pattern = re.compile('2|3|4')
        valid_input = False
        while not valid_input:
            len_input = input(MESSAGE_GET_LENGTH_INPUT)
            while not pattern.match(len_input):
                report(ERROR_CAR_LEN)
                len_input = input(MESSAGE_GET_LENGTH_INPUT)
            valid_input = True
        return int(len_input)

    def get_location_input(board_size):
        pattern = re.compile('^( )*[0-9]+( )*,( )*[0-9]+( )*$')
        valid_input = False
        while not valid_input:
            loc_input = input(MESSAGE_GET_LOCATION_INPUT)
            while not pattern.match(loc_input):
                report(ERROR_WRONG_INPUT_FORMAT)
                loc_input = input(MESSAGE_GET_LOCATION_INPUT)
            coordinate = tuple([int(x.strip()) for x in loc_input.split(',')])
            if min(coordinate) >= 0 and max(coordinate) < board_size:
                valid_input = True
            else:
                report(ERROR_COORDINATE_OUT_OF_BOUND + str(board_size-1))
        return coordinate

    def get_orientation_input():
        pattern = re.compile('0|1')
        valid_input = False
        while not valid_input:
            orn_input = input(MESSAGE_GET_ORIENTATION_INPUT)
            while not pattern.match(orn_input):
                report(ERROR_CAR_ORN)
                orn_input = input(MESSAGE_GET_ORIENTATION_INPUT)
            valid_input = True
        return int(orn_input)

    color = get_color_input()
    length = get_length_input()
    location = get_location_input(board_size)
    orientation = get_orientation_input()
    return color, length, location, orientation


def get_direction():
    """
    Get users input of the direction to move the car.
    :return: An object of the class direction representing the desired direction to move the car
    """
    pattern = re.compile(str(Direction.UP) + '|' + str(Direction.DOWN) + '|' + str(Direction.RIGHT) + '|'
                         + str(Direction.LEFT))
    valid_input = False
    while not valid_input:
        dirc_input = input(MESSAGE_GET_DIRECTION_INPUT)
        while not pattern.match(dirc_input):
            report(ERROR_DIRECTION)
            dirc_input = input(MESSAGE_GET_DIRECTION_INPUT)
        valid_input = True
    return int(dirc_input)

def report_game_over():
    """
    Report to user the game has ended successfully.
    :return: None
    """
    report(MESSAGE_GAME_OVER)


