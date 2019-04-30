from tkinter import *

class Board:
    def __init__(self):
        root = Tk()
        root.configure(bg="white", cursor="@assets/cursor_blue.cur")
        root.title("Connect Four")
        def key(event):
            print("pressed", repr(event.char))
        def callback(event):
            return event.x, event.y
        canvas = Canvas(width=700, height=600, bg='white')
        photo = PhotoImage(file='assets/empty.gif')
        for c in range(7):
            for r in range(6):
                canvas.create_image(100*c, 100*r, image=photo, anchor=NW)
        canvas.bind("<Key>", key)
        canvas.bind("<Button-1>", callback)
        canvas.pack()
        root.mainloop()

if __name__ == '__main__':
    Board()

