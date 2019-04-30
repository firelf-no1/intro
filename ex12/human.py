from communicator import Communicator
from tkinter import *
from PIL import Image
from math import floor

PLAYER_1 = 0
PLAYER_2 = 1
BOARDWIDTH = 7  # how many spaces wide the board is
BOARDHEIGHT = 6 # how many spaces tall the board is


class Human:
    def __init__(self, player, game, port, ip=None):
        self.game = game
        self.canvas = game.canvas
        self.counter = 0

        def callback(event):
            self.counter += 1
        self.canvas.bind("<Button-1>", self.getMove, callback)
        self.b_counter = 0
        self.player = player
        if self.player == PLAYER_1:
            self.color = 'b'
        else:
            self.color = 'r'
        self.__communicator = Communicator(self.canvas, port, ip)
        self.__communicator.connect()
        self.__communicator.bind_action_to_message(self.read_message)
        self.canvas.mainloop()

    def read_message(self, text=None):
        if text:
            if len(text) == 1:
                if self.color == 'b':
                    self.game.player2_message = 1
                if self.color == 'r':
                    self.game.player1_message = 1
                column = int(text)
                self.game.make_move(column)
                self.b_counter = 0
            else:
                if self.color == 'b':
                    self.game.player2_message = 1
                if self.color == 'r':
                    self.game.player1_message = 1
                text_list = []
                for i in range(len(text)):
                    if text[i].is_numeric():
                        text_list.append(text[i])
                if len(text_list) > 0:
                    column = int(text_list[0])
                    self.game.make_move(column)
                    self.b_counter = 0

    def getMove(self, event):
        x = floor((event.x - 139) / 75)
        y = floor((event.y - 150) / 75)
        column, row = self.move_check(x, y)
        try:
            if self.counter <= 1:
                if PLAYER_1 == self.player:
                    if self.game.turn_counter % 2 == 0:
                        self.game.make_move(column)
                        self.__communicator.send_message(str(column))
                        self.game.player2_message = 0
                        self.game.mylist_player2 = []
                        self.game.waiting_player_2()
                    else:
                        if self.game.win_status == 0:
                            self.its_not_your_turn()
                        else:
                            self.game.illegal_move()
                else:
                    if self.game.turn_counter % 2 == 0:
                        if self.game.win_status == 0:
                            self.its_not_your_turn()
                        else:
                            self.game.illegal_move()
                    else:
                        self.game.make_move(column)
                        self.__communicator.send_message(str(column))
                        self.game.player1_message = 0
                        self.game.mylist_player1 = []
                        self.game.waiting_player_1()

        except TypeError:
            self.game.illegal_move()

    def its_not_your_turn(self):
        if self.b_counter < 1:
            b = Button(text="it's not your turn please wait", height=4,
                                  width = 20)
            self.b_counter += 1

            def forget():
                b.place_forget()
                self.b_counter = 0
            b.place(relx=0.4, rely=0.435)
            b.config(command=forget)

    def move_check(self, column, row):
        # Returns True if there is an empty space in the given column.
        # Otherwise returns False.
        if column < 0 or column >= BOARDWIDTH or row < 0 or row >= BOARDHEIGHT:
            return '10&', '50$'
        n_row = self.game.get_lowest_empty_space(self.game.new_board, column)
        if n_row == 10:
            return '10&', '50$'
        return column, row

