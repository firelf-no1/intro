##############################################################
# FILE : ex11.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: solving a sudoku board
#############################################################
from ex11_backtrack import general_backtracking

BIG_SQUARE_SIZE = 9
SMALL_SQUARE_SIZE = 3
LEGAL_NUMBERS_RANGE = range(1, 10)

def print_board(board, board_size=9):
    """ prints a sudoku board to the screen

    ---  board should be implemented as a dictinary 
         that points from a location to a number {(row,col):num}
    """ 
    for row in range(board_size):
        if row%int(board_size**0.5) == 0:
            print('-------------')
        toPrint = ''
        for col in range(board_size):
            if col%int(board_size**0.5) == 0:
                toPrint += '|'
            toPrint += str(board[(row,col)])
        toPrint += '|'
        print(toPrint)
    print('-------------')


def load_game(sudoku_file):
    """
    :param sudoku_file: a txt file with a sudoku board
    :return: a board dict with the sudoku game
    """
    board = {}
    f_board = open(sudoku_file, 'r')
    row_number = 0
    for line in f_board:
        row_number += 1
        row = line.strip()
        n_row = []
        for i in range(len(row)):
            if row[i].isdigit():
                n_row.append(row[i])
        for j in range(len(n_row)):
            board[row_number - 1, j] = int(n_row[j])
    f_board.close()
    return board


def check_row(board, i, j):
    """
    checks the validation of a row
    :param board: a suduku board
    :param i: the row we are working on
    :param j: the column we are working on
    :return: true if all is ok and false if its not
    """
    for k in range(BIG_SQUARE_SIZE):
        if k != j:
            if board.get((i, k)) == board.get((i, j)):
                return False
            else:
                continue
    return True


def check_column(board, i, j):
    """
    checks the validation of a column
    :param board: a suduku board
    :param i: the row we are working on
    :param j: the column we are working on
    :return: true if all is ok and false if its not
    """
    for k in range(BIG_SQUARE_SIZE):
        if k != i:
            if board.get((k, j)) == board.get((i, j)):
                return False
            else:
                continue
    return True


def check_square(board, i, j):
    """
    checks the validation of a square
    :param board: a suduku board
    :param i: the row we are working on
    :param j: the column we are working on
    :return: true if all is ok and false if its not
    """
    col_start = j - j % SMALL_SQUARE_SIZE
    row_start = i - i % SMALL_SQUARE_SIZE
    for n in range(SMALL_SQUARE_SIZE):
        for z in range(SMALL_SQUARE_SIZE):
            if n + row_start != i and z + col_start != j:
                if board.get(((n + row_start), (z + col_start))) ==\
                        board.get((i, j)):
                    return False
                else:
                    continue
    return True


def check_board(board, x, *args):
    """

    :param board: Dictionary Similar to the structure described in the
                  previous function
    :param x: A tuple representing a position in the sudoku table
              (column, row)
    :param args: an extra input to the check bord that is not in use
    :return: returns true if the bord is ok and false if the bord has a problem
    """
    i = x[0]
    j = x[1]
    if check_row(board, i, j) and check_column(board, i, j) and \
        check_square(board, i, j):
        return True
    else:
        return False


def empty_position_exists(board, list_of_items):
    """
    update the list of empty position
    :param board: a suduko bord
    :param list_of_items: the list of empty position
    :return: an updated list
    """
    for row in range(BIG_SQUARE_SIZE):
        for col in range(BIG_SQUARE_SIZE):
            if board.get((row, col)) == 0:
                list_of_items.append((row, col))
    return list_of_items


def run_game(sudoku_file, print_mode = False):
    """
    the main function of the game
    :param sudoku_file: file that contains a sudoku table
    :param print_mode: Accepted as False. If the user wants to print the board
                       he needs to input true in the run commend
    :return: True or false depending on the solution of the board if the user
             changes the print mode to true it will print the bord if we have
             a solution
    """
    board = load_game(sudoku_file)
    set_of_assignments = LEGAL_NUMBERS_RANGE
    list_of_items = empty_position_exists(board, [])
    print(list_of_items)
    if general_backtracking(list_of_items, board, 0, set_of_assignments,
                            check_board):
        if print_mode:
            print_board(board)
        return True
    else:
        if print_mode:
            print_board(board)
        return False
