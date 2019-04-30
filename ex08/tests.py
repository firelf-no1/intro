import random

def exit_board1(size):
    board1 = [['_' for i in range(size + 1)] for i in range(size + 1)]
    for i in range(0, size):
        board1[i][0] = str(i)
        board1[size][i + 1] = str(i)
    x = random.randint(0, 1)
    y = random.randint(0, size - 1)
    if x == 0:
        board1[y][0] = 'E'
    elif x == 1:
        board1[size][y + 1] = 'E'
    exit_board = r_car(board1)
    flattened_list = [y for x in exit_board for y in x]
    brd = str()
    for i in range(len(board1)):
        for j in range(len(board1))
            row = flattened_list[i+j]
        brd = brd + '\n' + row

    return


def chaking_range(x, k):
    if int(2 + k - x - 1) == int(k - 1):
        z = int(k - 1)
        return z
    elif int(2 + k - x - 1) != int(k - 1):
        z = random.randint((2 + k - x), (k - 1))
        return z


def r_car(board1):
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


print((exit_board1(6)))