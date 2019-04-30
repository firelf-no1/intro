from human import Human
from ai import AI
from game import Game
from tkinter import *
from sys import platform


def args_check(args):
    if len(args) > 4 or len(args) < 3:
        print("Illegal program arguments")
        return False
    else:
        if int(args[2]) < 1000 or int(args[2]) > 65536:
            print("Illegal port")
            return False
        else:
            return True


def main(argv):
    if not args_check(argv):
        quit()
    else:
        port = int(argv[2])
        if len(argv) == 4:
            ip = argv[3]
        else:
            ip = None
        character = argv[1].lower()

        if ip == None:
            if platform == 'linux':
                root.root.configure(bg="white",
                                    cursor="dot blue blue")
                root.root.title("Connect Four - server")
                if character == 'is_human':
                    Human(0, root, port)
                else:
                    AI(0, root, port)
            if platform == 'win32':
                root.root.configure(bg="white",
                                    cursor="@assets/cursor_blue.cur")
                root.root.title("Connect Four - server")
                if character == 'is_human':
                    Human(0, root, port)
                else:
                    AI(0, root, port)
            else:
                root.root.title("Connect Four - client")
                if character == 'is_human':
                    Human(1, root, port, ip)
                else:
                    AI(1, root, port, ip)
        else:
            if platform == 'linux':
                root.root.configure(bg="white",
                                    cursor="dot red red")
                root.root.title("Connect Four - client")
                if character == 'is_human':
                    Human(1, root, port, ip)
                else:
                    AI(1, root, port, ip)
            if platform == 'win32':
                root.root.configure(bg="white",
                                    cursor="@assets/cursor_red.cur")
                root.root.title("Connect Four - client")
                if character == 'is_human':
                    Human(1, root, port, ip)
                else:
                    AI(1, root, port, ip)
            else:
                root.root.title("Connect Four - client")
                if character == 'is_human':
                    Human(1, root, port, ip)
                else:
                    AI(1, root, port, ip)


if __name__ == "__main__":
    """runs main"""
    root = Game()
    main(sys.argv)




