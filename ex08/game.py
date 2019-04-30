############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction
from board import Board
import random
############################################################
# Class definition
############################################################




class Game:
    """
    A class representing a rush hour game.
    A game is composed of cars that are located on a square board and a user
    which tries to move them in a way that will allow the red car to get out
    through the exit
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self._board = board

        print_board = self._board
        print('\n'.join(print_board))
        red_car_board = r_car(print_board)
        print('\n'.join(red_car_board))
        self._board = red_car_board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        The function runs one round of the game :
            1. Print board to the screen
            2. Get user's input of: what color car to move, and what direction to
                move it.
            2.a. Check the the input is valid. If not, print an error message and
                return to step 2.
            2. Move car according to user's input. If movement failed (trying
                to move out of board etc.), return to step 2.
            3. Report to the user the result of current round ()
        """
        color_input = input(gh.MESSAGE_GET_COLOR_INPUT)



    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

############################################################
# An example usage of the game
############################################################
def main():
    size1 = 6
    brd = Board.exit_board1(Board(cars = Car, exit_board = None, size = size1))
    brd_list = '\n'.join(brd)
    print(brd_list)

    while not done(brd_list):


if __name__=="__main__":
    size1 = 6
    board = Board(cars = Car, exit_board = exit_board1(size1) , size = size1)
    game = Game(board)
    game.play()
