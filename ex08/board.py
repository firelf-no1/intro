############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction
import random
############################################################
# Constants
############################################################

# place your constants here

############################################################
# Class definition
############################################################




class Board():
    """
    A class representing a rush hour board.
    """

    def __init__(self, cars, exit_board, size=6):
        """
        Initialize a new Board object.
        :param cars: A list (or dictionary) of cars.
        :param size: Size of board (Default size is 6). 
        """
        self.cars = cars
        self.exit_board = exit_board
        self.size = size

    def exit_board1(self):
        size = self.size
        board1 = [['_' for i in range(self.size + 1)] for i in range(size + 1)]
        for i in range(0, size):
            board1[i][0] = str(i)
            board1[size][i + 1] = str(i)
        x = random.randint(0, 1)
        y = random.randint(0, size - 1)
        if x == 0:
            board1[y][0] = 'E'
        elif x == 1:
            board1[size][y + 1] = 'E'
        return board1


    def get_num_cars(self):
        x = gh.get_num_cars()
        return x


    def chaking_range(self, x, k):
        if int(2 + k - x - 1) == int(k - 1):
            z = int(k - 1)
            return z
        elif int(2 + k - x - 1) != int(k - 1):
            z = random.randint((2 + k - x), (k - 1))
            return z

    def r_car(self.exit_board1()):
        board1 =
        x = random.randint(2, 4)
        k = len(board1)
        z = int(chaking_range(x, k))
        t = random.randint(0, k - x - 2)
        for i in range(k):
            if board1[i][0] == 'E':
                for j in range(x):
                    board1[i][z - j] = 'R'
            elif board1[k - 1][i] == 'E':
                for j in range(x):
                    board1[t + j][i] = 'R'
        return board1

    def add_car(self, car):
        """
        Add a single car to the board.
        :param car: A car object
        :return: True if a car was succesfuly added, or False otherwise.
        """
        color, length, location, orientation = car
        x, y = location
        board = self.exit_board
        if orientation == 0:
            if y + length <= len(board) - 1:
                counter = 0
                for i in range(length):
                    if not Board.is_empty(self, (x, y + i)):
                        counter = 0
                    else:
                        counter += 1
                if counter == length:
                    for i in range(length):
                        board[x][y + i] = color
            else:
                gh.report(gh.ERROR_COORDINATE_OUT_OF_BOUND)
        if orientation == 1:
            if x + length <= len(board) - 1:
                counter = 0
                for i in range(length):
                    if not Board.is_empty(self, (x + i, y)):
                        counter = 0
                    else:
                        counter += 1
                if counter == length:
                    for i in range(length):
                        board[x + i][y] = color
            else:
                gh.report(gh.ERROR_COORDINATE_OUT_OF_BOUND)
        return board

    def final_board(self):
        x = self.get_num_cars()
        board = self.exit_board
        car = [[] for k in range(x)]
        for i in range(x):
            car[i] = gh.get_car_input(self.size)
            board = self.add_car(car[i])
        return board

    def get_location(self):
        """
        location getter
        """
        return self.__location

    def is_empty(self, location):
        """
        Check if a given location on the board is free.
        :param location: x and y coordinations of location to be check
        :return: True if location is free, False otherwise
        """
        # x, y = location
        board = self.exit_board
        # if board[x][y] == '_':
        #     return True
        # else:
        #     return False
        if not 1 <= location[0] < len(board) or not 1 <= location[1] < len(board):
            return False
        for car in self.cars:
            if location == car.get_location():
                return False
        for tree in self.trees:
            if location == tree:
                return False
        if self.hero:
            if location == self.hero.get_location():
                return False
        return True
    
    def move(self, car, direction):
        """
        Move a car in the given direction.
        :param car: A Car object to be moved.
        :param direction: A Direction object representing desired direction
            to move car.
        :return: True if movement was possible and car was moved, False otherwise.
        """
        color, length, location, orientation = car
        new_location = location[:]
        if orientation == 0:
            if direction == Direction.UP:
                new_location[0] -= 1
            elif direction == Direction.DOWN:
                new_location[0] += 1
            else:
                gh.report(gh.ERROR_DIRECTION)
        if orientation == 1:
            if direction == Direction.LEFT:
                new_location[1] -= 1
            elif direction == Direction.RIGHT:
                new_location[1] += 1
            else:
                gh.report(gh.ERROR_DIRECTION)
        if Board.is_empty(self, new_location):
            location = new_location
        return location

    def bord_end(self, ):
    def __repr__(self):
        """
        :return: Return a string representation of the board.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass
