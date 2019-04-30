from tkinter import *
from communicator import Communicator
import copy
import random
from time import time
PLAYER_1 = 0
PLAYER_2 = 1
BOARDWIDTH = 7  # how many spaces wide the board is
BOARDHEIGHT = 6 # how many spaces tall the board is
DIFFICULTY = 3


class AI:
    def __init__(self, player, game, port, ip=None):
        self.game = game
        self.canvas = game.canvas
        self.player = player
        self.__communicator = Communicator(self.canvas, port, ip)
        self.__communicator.connect()
        self.__communicator.bind_action_to_message(self.read_message)
        self.difficulty = DIFFICULTY
        if self.player == PLAYER_1:
            self.color = 'b'
            if self.game.turn_counter % 2 == 0:
                self.game.make_move(3)
                self.__communicator.send_message(str(3))
                self.game.player2_message = 0
                self.game.mylist_player2 = []
                self.game.waiting_player_2()
        else:
            self.color = 'r'
        self.counter = 0
        self.b_column_counter = 0
        self.b_counter = 0
        self.canvas.bind("<Button-1>", self.illegal_move)
        self.b_illegal_counter = 0
        self.canvas.mainloop()

    def read_message(self, text=None):
        if text:
            if len(text) == 1:
                column = int(text)
                self.game.make_move(column)
                if self.color == 'b':
                    self.game.player2_message = 1
                if self.color == 'r':
                    self.game.player1_message = 1
                self.find_legal_move(self.game, func=None)
            else:
                text_list = []
                for i in range(len(text)):
                    if text[i].is_numeric():
                        text_list.append(text[i])
                if len(text_list) > 0:
                    column = int(text_list[0])
                    self.game.make_move(column)
                    if self.color == 'b':
                        self.game.player2_message = 1
                    if self.color == 'r':
                        self.game.player1_message = 1
                    self.find_legal_move(self.game, func=None)

    def illegal_move(self, event):
        if self.b_illegal_counter < 1:
            b = Button(text="Illegal move", height=4,
                       width=20)
            self.b_illegal_counter += 1

            def forget():
                b.place_forget()
                self.b_illegal_counter = 0
            b.place(relx=0.4, rely=0.435)
            b.config(command=forget)

    def find_legal_move(self, g, func, timeout=None):
        if g.win_status == 0:
            if timeout == None:
                try:
                    column = self.get_ai_move(g.new_board, DIFFICULTY,
                                              func=None)
                    g.make_move(column)
                    self.__communicator.send_message(str(column))
                    if self.color == 'b':
                        g.player2_message = 0
                        g.mylist_player2 = []
                        g.waiting_player_2()
                    else:
                        g.player1_message = 0
                        g.mylist_player1 = []
                        g.waiting_player_1()
                except IndexError:
                    self.no_move()
            else:
                column = self.get_ai_move(g.new_board, DIFFICULTY, func)
                g.make_move(column)
                self.__communicator.send_message(str(column))



    def get_ai_move(self, board, depth, func):
        """ Returns the best move (as a column number) and the associated alpha
            Calls search()
        """
        # determine opponent's color
        if self.color == 'b':
            enemy_tile = 'r'
        else:
            enemy_tile = 'b'
        # enumerate all legal moves
        legal_moves = {}  # will map legal move states to their alpha values
        for col in range(BOARDWIDTH):
            # if column i is a legal move...
            if self.move_check(board, col):
                # make the move in column 'col' for curr_player
                temp = self.make_a_move(board, self.color, col)
                legal_moves[col] = -self.search(depth-1, temp, enemy_tile)
                max_move = max(legal_moves.values())
                if func != None:
                    func(list(legal_moves.keys())[list(legal_moves.values())
                    .index(max_move)])

        best_alpha = -99999999
        best_move = []
        moves = legal_moves.items()
        for move, alpha in moves:
            if alpha > best_alpha:
                best_alpha = alpha
                best_move = []
                best_move.append(move)
            if alpha == best_alpha:
                best_move.append(move)
        if len(best_move) > 1:
            return random.choice(best_move)
        if len(best_move) == 1:
            return best_move[0]
        else:
            raise IndexError


    def search(self, depth, board, tile):
        """ Searches the tree at depth 'depth'

            Returns the alpha value
        """

        # enumerate all legal moves from this state
        legal_moves = []
        for column in range(BOARDWIDTH):
            # if column is a legal move...
            if self.move_check(board, column):
                # make the move in column for curr_player
                temp = self.make_a_move(board, tile, column)
                legal_moves.append(temp)

        # if this node (state) is a terminal node or depth == 0...
        if depth == 0 or len(legal_moves) == 0 or self.board_full_check(board):
            # return the heuristic value of node
            return self.value(board, tile)

        # determine opponent's color
        if tile == 'b':
            enemy_tile = 'r'
        else:
            enemy_tile = 'b'

        alpha = -99999999
        for child in legal_moves:
            try:
                if child != None:
                    alpha = max(alpha, -self.search(depth - 1, child,
                                                    enemy_tile))
                else:
                    raise TypeError
            except TypeError:
                self.no_move()
        return alpha

    def value(self, board, tile):
        if tile == 'b':
            enemy_tile = 'r'
        else:
            enemy_tile = 'b'
        my_fours = self.check_for_streak(board, tile, 4)
        my_threes = self.check_for_streak(board, tile, 3)
        my_twos = self.check_for_streak(board, tile, 2)
        enemy_fours = self.check_for_streak(board, enemy_tile, 4)
        enemy_threes = self.check_for_streak(board, enemy_tile, 3)
        enemy_twos = self.check_for_streak(board, enemy_tile, 2)
        if enemy_fours > 0:
            return -100000 - DIFFICULTY
        else:
            return (my_fours*100000 + my_threes*100 + my_twos*10) - \
               (enemy_threes*100 + enemy_twos*10)\
               + DIFFICULTY

    def check_for_streak(self, board, color, streak):
        count = 0
        # for each piece in the board...
        for i in range(BOARDWIDTH):
            for j in range(BOARDHEIGHT-1, -1, -1):
                # ...that is of the color we're looking for...
                if board[i][j] == color:
                    # check if a vertical streak starts at (i, j)
                    count += self.vertical_streak(j, i, board, streak)

                    # check if a horizontal four-in-a-row starts at (i, j)
                    count += self.horizontal_streak(j, i, board, streak)

                    # check if a diagonal (either way) four-in-a-row starts at (i, j)
                    count += self.diagonal_check(j, i, board, streak)

        # return the sum of streaks of length 'streak'
        return count

    def vertical_streak(self, row, col, board, streak):
        consecutive_count = 0
        for i in range(streak):
            if row - i < 0:
                break
            if board[col][row] == board[col][row - i]:
                consecutive_count += 1
        if consecutive_count >= streak:
            return 1
        else:
            return 0

    def horizontal_streak(self, row, col, board, streak):
        consecutive_count = 0
        for i in range(streak):
            if col + i >= BOARDWIDTH:
                break
            if board[col][row] == board[col + i][row]:
                consecutive_count += 1
        if consecutive_count >= streak:
            return 1
        else:
            return 0

    def diagonal_check(self, row, col, board, streak):

        total = 0
        # check for diagonals with positive slope
        consecutive_count = 0
        for i in range(streak):  # check the first 4 columns
            if col + i > BOARDWIDTH-1 or row - i < 0:
                break
            if board[col][row] == board[col + i][row - i]:
                consecutive_count += 1
        if consecutive_count >= streak:
            total += 1
        # check for diagonals with negative slope
        consecutive_count = 0
        for i in range(streak):
            if col + i > BOARDWIDTH-1 or row + i > BOARDHEIGHT-1:
                break
            if board[col][row] == board[col + i][row + i]:
                consecutive_count += 1
        if consecutive_count >= streak:
            total += 1

        return total

    def make_a_move(self, board, player, column):
        practice_board = copy.deepcopy(board)
        lowest = self.get_lowest_empty_space(practice_board, column)
        if lowest != -1:
            practice_board[column][lowest] = player
        return practice_board

    def get_lowest_empty_space(self, board, column):
        # Return the row number of the lowest empty row in the given column.
        for y in range(BOARDHEIGHT-1, -1, -1):
            if board[column][y] == 'e':
                return y
        return -1

    def board_full_check(self, board):
        # Returns True if there are no empty spaces anywhere on the board.
        for x in range(BOARDWIDTH):
            if board[x][0] == 'e':
                return False
        return True

    def move_check(self, board, column):
        # Returns True if there is an empty space in the given column.
        # Otherwise returns False.
        if column < 0 or column >= (BOARDWIDTH) or board[column][0] != 'e':
            return False
        return True

    def no_move(self):
        """
        a graphic representations of an illegal move
        :return:
        """
        if self.b_counter < 1:
            self.b = Button(text="No possible AI moves", height=4,
                            width=20)
            self.b_counter += 1

            def forget():
                self.b.place_forget()
                self.b_column_counter = 0

            self.b.place(relx=0.4, rely=0.435)
            self.b.config(command=forget)
