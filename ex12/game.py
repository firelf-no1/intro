from tkinter import *
from sys import platform
from PIL import Image, ImageTk, ImageSequence

BOARDWIDTH = 7  # how many spaces wide the board is
BOARDHEIGHT = 6 # how many spaces tall the board is
assert BOARDWIDTH >= 4 and BOARDHEIGHT >= 4, 'Board must be at least 4x4'
WIDESINGELPIC = 75
WIDTHBUFFER = 140
HEIGHTBUFER = 150
CANVASWIDTH = 800
CANVASHEIGHT = 600




class Game:

    PLAYER_ONE = 0
    PLAYER_TWO = 1
    DRAW = 2

    def __init__(self):
        """
        initiate the board
        """
        self.root = Tk()
        self.background = PhotoImage('assets/background.gif')
        self.canvas = Canvas(width=CANVASWIDTH, height=CANVASHEIGHT)
        self.tower = Image.open("assets/background1.gif")
        self.tower_tk = ImageTk.PhotoImage(self.tower)
        self.try_list_player1 = []
        self.try_list_player2 = []
        self.canvas.place(x=0, y=0, anchor='nw')
        self.canvas.create_image(0, 0, image=self.tower_tk, anchor='nw')
        self.canvas.image = self.tower_tk
        self.frame = Frame(self.root)
        self.frame.place(x=CANVASWIDTH, y=CANVASHEIGHT, anchor='se')
        self.player1 = Image.open("assets/player1.gif")
        self.player1_tk = ImageTk.PhotoImage(self.player1)
        self.try_list_player1.append(self.canvas.create_image(-5, HEIGHTBUFER,
                                                              image=
                                                              self.player1_tk,
                                                              anchor='nw'))
        self.canvas.image = self.player1_tk
        self.player2 = Image.open("assets/player2.gif")
        self.player2_tk = ImageTk.PhotoImage(self.player2)
        self.try_list_player2.append(self.canvas.create_image(650, HEIGHTBUFER,
                                                              image=
                                                              self.player2_tk,
                                                              anchor='nw'))
        self.canvas.image = self.player2_tk
        self.empty_photo = PhotoImage(file="assets/empty.gif")  # All slots
        for c in range(BOARDWIDTH):
            for r in range(BOARDHEIGHT):
                self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC * c),
                                         HEIGHTBUFER + (WIDESINGELPIC * r),
                                         image=self.empty_photo,
                                         anchor="nw")
        self.blue_photo = PhotoImage(file="assets/blue.gif")  # Blue slots
        self.red_photo = PhotoImage(file="assets/red.gif")  # Red slots
        self.blue_win_photo = PhotoImage(file="assets/blue_win.gif")  # Blue
                                                                      # slots
        self.red_win_photo = PhotoImage(file="assets/red_win.gif")  # Red slots
        self.blue_win = 'assets/bluewin.gif'
        self.red_win = 'assets/redwin.gif'
        self.tie_win = 'assets/tiewin.gif'
        self.turn_counter = 0  # keeps track of number of turns
        self.win_status = 0  # 0 when playing, 1 when won
        self.new_board = []
        self.get_new_board()
        self.r_ord = 0
        self.c_ord = 0
        self.frame_status = 0
        self.total_frame_num = 21  # length of GIF anim in frames
        self.frame_delay = 30  # in ms
        # button slide variables
        self.current_height = -0.1  # also the starting height
        self.final_height = 0.32  # actual stopping height will be greater
                                  # and a multiple of increment_height
        self.increment_height = 0.02  # as a proportion of the window space
        # cursor animation variables
        self.cursor_state = 0
        self.image_state_player1 = 0
        self.image_state_player2 = 0
        self.player1_message = 1
        self.player2_message = 1
        self.cursor_total_states = 17  # multiples of 8 + 1 for the full loop
        self.cursor_delay = WIDESINGELPIC
        self.b_illegal_counter = 0
        self.b_column_counter = 0
        self.mylist_player1 = []
        self.mylist_player2 = []
        self.canvas.pack(side="top", fill="both", expand="yes")

    def get_new_board(self):
        """
        initiate a new board
        :return: a new list of list that represent the board
        """
        board = []
        for x in range(BOARDWIDTH):
            board.append(['e'] * BOARDHEIGHT)
        self.new_board = board

    def make_move(self, column):
        """
        makes a move on the board
        :param column: the column that the pice is going to
        :return:
        """
        x = self.get_current_player()
        if x == 0 and self.win_status == 0:
            color = 'b'
        else:
            color = 'r'
        self.drop_piece(column, color)

    def waiting_player_1(self):
        """
        a spinning head graphic while the player is waiting for the other side
         to make a move
        :return:
        """
        self.images = ["assets/player1-0.gif",
                       "assets/player1-1.gif",
                       "assets/player1-2.gif",
                       "assets/player1-3.gif",
                       "assets/player1-4.gif",
                       "assets/player1-5.gif",
                       "assets/player1-6.gif",
                       "assets/player1-7.gif",
                       "assets/player1-0.gif"]
        self.canvas.delete(self.try_list_player1[len(self.try_list_player1)-1])
        self.wait_player1 = Image.open(self.images[self.image_state_player1
                                                   % 8])
        self.wait_player1_tk = ImageTk.PhotoImage(self.wait_player1)
        self.mylist_player1.append(self.canvas.create_image(-5, HEIGHTBUFER,
                                                    image=self.wait_player1_tk,
                                                    anchor='nw'))
        self.canvas.image = self.wait_player1_tk
        self.image_state_player1 += 1
        if self.image_state_player1 < self.cursor_total_states:
            if self.player1_message == 0 and self.win_status == 0:
                self.root.after(self.cursor_delay,
                                                   self.waiting_player_1)
            else:
                for i in range(len(self.mylist_player1)):
                    self.canvas.delete(self.mylist_player1[i])
                self.player1 = Image.open("assets/player1.gif")
                self.player1_tk = ImageTk.PhotoImage(self.player1)
                self.try_list_player1.append(self.canvas.create_image
                                             (-5, HEIGHTBUFER,
                                              image=self.player1_tk,
                                              anchor='nw'))
                self.canvas.image = self.player1_tk
        if self.image_state_player1 == self.cursor_total_states:
            if self.player1_message == 0 and self.win_status == 0:
                self.image_state_player1 = 0
                self.root.after(self.cursor_delay,
                                self.waiting_player_1)
            else:
                for i in range(len(self.mylist_player1)):
                    self.canvas.delete(self.mylist_player1[i])
                self.player1 = Image.open("assets/player1.gif")
                self.player1_tk = ImageTk.PhotoImage(self.player1)
                self.try_list_player1.append(self.canvas.create_image(-5,
                                             HEIGHTBUFER,
                                             image=self.player1_tk,
                                             anchor='nw'))
                self.canvas.image = self.player1_tk

    def waiting_player_2(self):
        """
        a spinning head graphic while the player is waiting for the other side
         to make a move
        :return:
        """
        self.images = ["assets/player2-0.gif",
                       "assets/player2-1.gif",
                       "assets/player2-2.gif",
                       "assets/player2-3.gif",
                       "assets/player2-4.gif",
                       "assets/player2-5.gif",
                       "assets/player2-6.gif",
                       "assets/player2-7.gif",
                       "assets/player2-0.gif"]
        self.canvas.delete(self.try_list_player2[len(self.try_list_player2)-1])
        self.wait_player2 = Image.open(self.images[self.image_state_player2
                                                   % 8])
        self.wait_player2_tk = ImageTk.PhotoImage(self.wait_player2)
        self.mylist_player2.append(self.canvas.create_image(650, HEIGHTBUFER,
                                                    image=self.wait_player2_tk,
                                                    anchor='nw'))
        self.canvas.image = self.wait_player2_tk
        self.image_state_player2 += 1
        if self.image_state_player2 < self.cursor_total_states:
            if self.player2_message == 0 and self.win_status == 0:
                self.root.after(self.cursor_delay, self.waiting_player_2)
            else:
                for i in range(len(self.mylist_player2)):
                    self.canvas.delete(self.mylist_player2[i])
                self.player2 = Image.open("assets/player2.gif")
                self.player2_tk = ImageTk.PhotoImage(self.player2)
                self.try_list_player2.append(self.canvas.create_image
                                             (650, HEIGHTBUFER,
                                              image=self.player2_tk,
                                              anchor='nw'))
                self.canvas.image = self.player2_tk
        if self.image_state_player2 == self.cursor_total_states:
            if self.player2_message == 0 and self.win_status == 0:
                self.image_state_player2 = 0
                self.root.after(self.cursor_delay, self.waiting_player_2)
            else:
                for i in range(len(self.mylist_player2)):
                    self.canvas.delete(self.mylist_player2[i])
                self.player2 = Image.open("assets/player2.gif")
                self.player2_tk = ImageTk.PhotoImage(self.player2)
                self.try_list_player2.append(self.canvas.create_image(650,
                                             HEIGHTBUFER,
                                             image=self.player2_tk,
                                             anchor='nw'))
                self.canvas.image = self.player2_tk

    def get_winner(self):
        for i in range(len(self.new_board)):
            set(self.new_board[i])
        # check vertical conditions
        self.blue_vertical = ['b', 'b', 'b', 'b']
        self.red_vertical = ['r', 'r', 'r', 'r']
        for i in range(len(self.new_board)-1,-1,-1):
            if any(self.blue_vertical == self.new_board[i][j:j + 4] for j in \
                   range(3)):  # Blue verticals
                for j in range(3):
                    if self.blue_vertical == self.new_board[i][j:j+4]:
                        for x in range(j,j+4):
                            self.canvas.create_image(WIDTHBUFFER +
                                                     (WIDESINGELPIC * i),
                                                     HEIGHTBUFER +
                                                     (WIDESINGELPIC * x),
                                                     image=self.blue_win_photo,
                                         anchor="nw")
                self.win_status = 1
                self.load_frames(self.blue_win)
                self.display_win_message()
            if any(self.red_vertical == self.new_board[i][j:j + 4] for j in \
                   range(3)):  # Red verticals
                for j in range(3):
                    if self.blue_vertical == self.new_board[i][j:j+4]:
                        for x in range(j,j+4):
                            self.canvas.create_image(WIDTHBUFFER +
                                                     (WIDESINGELPIC * i),
                                                     HEIGHTBUFER +
                                                     (WIDESINGELPIC * x),
                                                     image=self.red_win_photo,
                                         anchor="nw")
                self.win_status = 1
                self.load_frames(self.red_win)
                self.display_win_message()

        # check horizontal conditions
        for i in range(4):  # only needs to check the first 4 columns
            for j in range(BOARDHEIGHT-1,-1,-1):  # check all 6 rows of each column
                subtotal = [self.new_board[i][j], self.new_board[i + 1][j],
                            self.new_board[i + 2][j], self.new_board[i + 3][j]]
                if subtotal == self.blue_vertical:  # Blue horizontals
                    for x in range(i,i+4):
                        self.canvas.create_image(WIDTHBUFFER +
                                                 (WIDESINGELPIC * x),
                                                 HEIGHTBUFER +
                                                 (WIDESINGELPIC * j),
                                                 image=self.blue_win_photo,
                                                 anchor="nw")
                    self.win_status = 1
                    self.load_frames(self.blue_win)
                    self.display_win_message()
                if subtotal == self.red_vertical:  # Red horizontals
                    for x in range(i,i+4):
                        self.canvas.create_image(WIDTHBUFFER +
                                                 (WIDESINGELPIC * x),
                                                 HEIGHTBUFER +
                                                 (WIDESINGELPIC * j),
                                                 image=self.red_win_photo,
                                                 anchor="nw")
                    self.win_status = 1
                    self.load_frames(self.red_win)
                    self.display_win_message()

        # check diagonal conditions
        for i in range(4):  # check the first 4 columns
            for j in range(3):  # check the top 3 rows. A SW->NE diagonal
                # can only start from the bottom three, or else
                # it will not fit.
                subtotal = [self.new_board[i][j], self.new_board[i + 1][j + 1],
                            self.new_board[i + 2][j + 2],
                            self.new_board[i + 3][j + 3]]
                if subtotal == self.blue_vertical:  # Blue diagonals SW->NE
                    for x in range(4):
                        self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC
                                                                * (i + x)),
                                                 HEIGHTBUFER +
                                                 (WIDESINGELPIC * (j + x)),
                                                 image=self.blue_win_photo,
                                                 anchor="nw")
                    self.win_status = 1
                    self.load_frames(self.blue_win)
                    self.display_win_message()
                if subtotal == self.red_vertical:  # Red diagonals SW->NE
                    for x in range(4):
                        self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC
                                                                * (i + x)),
                                                 HEIGHTBUFER +
                                                 (WIDESINGELPIC * (j + x)),
                                                 image=self.red_win_photo,
                                                 anchor="nw")
                    self.win_status = 1
                    self.load_frames(self.red_win)
                    self.display_win_message()
            for j in range(3,
                           BOARDHEIGHT):  #check the bottem 3 rows for the same
                                          #reason as above.
                subtotal = [self.new_board[i][j], self.new_board[i + 1][j - 1],
                            self.new_board[i + 2][j - 2],
                            self.new_board[i + 3][j - 3]]
                if subtotal == self.blue_vertical:  # Blue diagonals NW->SE
                    for x in range(4):
                        self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC
                                                                * (i + x)),
                                                 HEIGHTBUFER +
                                                 (WIDESINGELPIC * (j - x)),
                                                 image=self.blue_win_photo,
                                                 anchor="nw")
                    self.win_status = 1
                    self.load_frames(self.blue_win)
                    self.display_win_message()
                if subtotal == self.red_vertical:  # Red diagonals NW->SE
                    for x in range(4):
                        self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC
                                                                * (i + x)),
                                                 HEIGHTBUFER +
                                                 (WIDESINGELPIC * (j - x)),
                                                 image=self.red_win_photo,
                                                 anchor="nw")
                    self.win_status = 1
                    self.load_frames(self.red_win)
                    self.display_win_message()
        # check if board is full
        board_full = []
        board_not_full = ['e', 'e', 'e', 'e', 'e', 'e', 'e']
        counter = 0
        for i in range(BOARDWIDTH):
            board_full.append(self.new_board[i][0])
            if board_not_full[i] != board_full[i]:
                counter += 1
            else:
                counter = 0
        if counter == BOARDWIDTH:
            self.win_status = 1
            self.load_frames(self.tie_win)
            self.display_win_message()

    def get_player_at(self, row, col):
        x = self.new_board[col][row]
        if x != 'e':
            if x == 'b':
                return Game.PLAYER_ONE
            else:
                return Game.PLAYER_TWO

    def get_current_player(self):
        x = self.turn_counter
        if x % 2 == 0:
            return Game.PLAYER_ONE
        else:
            return Game.PLAYER_TWO

    def get_lowest_empty_space(self, board, column):
        # Return the row number of the lowest empty row in the given column.
        for y in range(5,-1,-1):
            if board[column][y] == 'e':
                return y
        return 10

    def redraw(self, c_ord, r_ord, piece_state):
        if piece_state == 'b':
            self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC * c_ord),
                                     HEIGHTBUFER + (WIDESINGELPIC * r_ord),
                                     image=self.blue_photo, anchor='nw')
        elif piece_state == 'r':
            self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC * c_ord),
                                     HEIGHTBUFER + (WIDESINGELPIC * r_ord),
                                     image=self.red_photo, anchor='nw')
        elif piece_state == 'e':
            self.canvas.create_image(WIDTHBUFFER + (WIDESINGELPIC * c_ord),
                                     HEIGHTBUFER + (WIDESINGELPIC * r_ord),
                                     image=self.empty_photo, anchor='nw')

    def drop_piece(self, c_ord, color):
        self.c_ord = c_ord
        self.r_ord = self.get_lowest_empty_space(self.new_board, self.c_ord)
        self.new_board[self.c_ord][self.r_ord] = color
        piece_state = self.new_board[self.c_ord][self.r_ord]
        self.turn_counter += 1
        self.redraw(self.c_ord, self.r_ord, piece_state)  # draws colored
        self.get_winner()

    def load_frames(self, team): # load animation frames.
        self.frames = []
        # loads each frame to the list self.frames
        for i in range(self.total_frame_num):
            self.frames.append(
                PhotoImage(file=team, format="gif -index " + str(i)))

    def place_buttons(self): # create the quit button
        self.button_quit = Button(text="Quit",
                                  command=quit,
                                  height=4,
                                  width=20)
        self.button_quit.place(relx=0.4, rely=self.current_height)
        self.animate_buttons()  # begin animation of buttons

    def animate_buttons(self): # animate the button
        # drop the quit buttons down
        if self.current_height < self.final_height:
            self.button_quit.place(rely=self.current_height)
            self.current_height += self.increment_height
            self.canvas.after(self.frame_delay, self.animate_buttons)

    def win_animation(self): # animate the main win banner
        try:
            self.winlabel = Label(background=None, image=self.frames[
                self.frame_status])  # creates label from first frame
            self.winlabel.place(relx=0.12, rely=0.48)
            if self.frame_status < self.total_frame_num:
                self.frame_status += 1  # cycles to next frame
            self.winlabel.configure(
                image=self.frames[self.frame_status - 1])  # refreshes frame
            if self.frame_status < self.total_frame_num:
                self.canvas.after(self.frame_delay,
                                  self.win_animation)  # keeps updating the image
                                                       # every 20ms
            else:
                self.place_buttons()
        except IndexError:
            self.place_buttons()  # triggers button fall AFTER animation
                                  # is complete to avoid a bug

    def cursor_animate(self):
        """
        JUST FOR FUN! only work on windows
        :return:
        """
        self.cursors = ["@assets/frame0.cur",
                        "@assets/frame1.cur",
                        "@assets/frame2.cur",
                        "@assets/frame3.cur",
                        "@assets/frame4.cur",
                        "@assets/frame5.cur",
                        "@assets/frame6.cur",
                        "@assets/frame7.cur",
                        "@assets/frame0.cur"]
        self.root.configure(cursor=self.cursors[self.cursor_state % 8])
        self.cursor_state += 1
        if self.cursor_state < self.cursor_total_states:
            self.cursoranim = self.root.after(self.cursor_delay,
                                              self.cursor_animate)

    def display_win_message(self):
        """
        initiates animations. Allows them to be split into their own methods.
        :return:
        """
        if platform == 'linux':
            self.win_animation()
            x = self.get_current_player()
            if x == 0:
                self.root.configure(cursor='man red red')
            else:
                self.root.configure(cursor='man blue blue')
        if platform == 'win32':
            self.win_animation()
            self.cursor_animate()
        else:
            self.win_animation()

    def illegal_move(self):
        """
        a graphic representations of an illegal move
        :return:
        """
        if self.b_column_counter < 1:
            self.b = Button(text="Illegal move", height=4,
                            width=20)
            self.b_column_counter += 1

            def forget():
                self.b.place_forget()
                self.b_column_counter = 0

            self.b.place(relx=0.4, rely=0.435)
            self.b.config(command=forget)


