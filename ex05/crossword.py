import sys
import os.path
from collections import Counter
NUMBER_OF_ARGUMENTS = 4
ERROR_MESSAGE_ARGUMENTS = "ERROR: invalid number of parameters." \
                          " Please enter word_file matrix_file" \
                          " output_file directions."
ERROR_MESSAGE_WORD_FILE = "ERROR: Word file word_list.txt does not exist."
ERROR_MESSAGE_MATRIX_FILE = "ERROR: Matrix file mat.txt does not exist."
ERROR_MESSAGE_DIRECTIONS = "ERROR: invalid directions."
WORD_FILE_LOCATION = 1
MATRIX_FILE_LOCATION = 2
OUTPUT_FILE_LOCATION = 3
DIRECTIONS_LOCATION = 4

x_list = list()
w_list = list()
u_list = list()
y_list = list()
z_list = list()
d_list = list()
l_list = list()
r_list = list()


def check_arg(arg_list):
    """ a progrem that chaecks if the input is ok"""
    if len(arg_list) != NUMBER_OF_ARGUMENTS + 1:
        print(ERROR_MESSAGE_ARGUMENTS)
        return False
    if not (os.path.isfile(arg_list[WORD_FILE_LOCATION]) and
            os.path.isfile(arg_list[MATRIX_FILE_LOCATION])):
        print(ERROR_MESSAGE_WORD_FILE)
        return False
    elif not os.path.isfile(arg_list[WORD_FILE_LOCATION]):
        print(ERROR_MESSAGE_WORD_FILE)
        return False
    elif not os.path.isfile(arg_list[MATRIX_FILE_LOCATION]):
        print(ERROR_MESSAGE_MATRIX_FILE)
        return False
    return True


def load_words(words_file_name):
    '''
    Loads a list of  words from a txt file
    '''
    words = []
    f_words = open(words_file_name, 'r')
    for line in f_words:
        word = line.strip()
        if word.isalpha():
            word1 = word.lower()
            words.append(word1)
    f_words.close()
    return words


def load_grid(matrix_file):
    '''
    Loads a grid of letters from a txt file
    '''
    grid = str()
    f_mat = open(matrix_file, 'r')
    for line in f_mat.readlines():
        line = line.replace(',', ' ')
        line1 = line.lower()
        grid = grid + line1
    f_mat.close()
    return grid


def f(grid, word):
    """finds the row and collom of a word"""
    w = (grid.find("\n") + 1)
    q = len(word)
    location = ",".join("%s,%s" %
                        (int(x / w + 1), int(x % w / 2 + 1))
                        for i in range(len(grid))
                        for j in (-w - 2, - w, - w + 2, - 2, 2,
                                  w - 2, w, w + 2)
                        for x in (i, i + (q - 1) * j)
                        if grid[i::j][:q].lower() == word)
    if location != [""]:
        location1 = location.split(",")
        word_times = int(len(location1) / 4)
        for i in range(0, word_times):
            r1 = location1[4 * i]
            c1 = location1[1 + (4 * i)]
            r2 = location1[2 + (4 * i)]
            c2 = location1[3 + (4 * i)]
            diraction(r1, c1, r2, c2, word)
    else:
        return 'no location'
    return location


def diraction(r1, c1, r2, c2, word):
    """finds the diraction of the word"""
    if r1 > r2:
        if c1 > c2:
            x_list.append(word)
        if c1 < c2:
            w_list.append(word)
        else:
            u_list.append(word)
    if r1 < r2:
        if c1 > c2:
            y_list.append(word)
        if c1 < c2:
            z_list.append(word)
        if c1 == c2:
            d_list.append(word)
    elif r1 == r2:
        if c1 > c2:
            l_list.append(word)
        if c1 < c2:
            r_list.append(word)


def letter_chack(f):
    """checks the direction of the user input"""
    if f == 'x':
        return x_list
    elif f == 'y':
        return y_list
    elif f == 'z':
        return z_list
    elif f == 'w':
        return w_list
    elif f == 'r':
        return r_list
    elif f == 'l':
        return l_list
    elif f == 'u':
        return u_list
    elif f == 'd':
        return d_list


def der_search(diraction_name):
    """checks if there is more than one direction in the user input"""
    name = diraction_name
    diraction2 = name.split()
    name_p = str()
    if len(diraction2) > 1:
        for k in range(0, len(diraction2)):
            name_p = name_p + str(letter_chack(diraction2(k)))
        return name, name_p
    else:
        name_p = letter_chack(name)
        return name, name_p


def word_search(grid, words):
    """runs the word search"""
    for i in range(0, len(words)):
        f(grid, words[i])


def output_diraction(output_file_name, diraction_name):
    """runs the output file writhing"""
    direction_name1 = ''.join(diraction_name)
    output_file = open(output_file_name, 'w')
    final_cnt = list()
    for i in range(0, len(direction_name1)):
        dire_file = diraction_name[i]
        name, name_p = der_search(dire_file)
        print(name)
        print(name_p)
        output_list = name_p
        hist = [[x, output_list.count(x)] for x in set(output_list)]
        final_file = sorted(hist)
        for k in range(0, len(final_file)):
            go = ",".join(str(x) for x in final_file[k])
            final_cnt.append(go)
    final_l = sorted(final_cnt)
    gone = ("\n".join(final_l))
    output_file.write(gone)
    output_file.close()


def main(argv):
    """main program"""
    if not check_arg(argv):
        return
    word_file = sys.argv[WORD_FILE_LOCATION]
    matrix_file = sys.argv[MATRIX_FILE_LOCATION]
    diraction_list = sys.argv[DIRECTIONS_LOCATION]
    output_file = sys.argv[OUTPUT_FILE_LOCATION]
    words = load_words(word_file)
    matrix = load_grid(matrix_file)
    word_search(matrix, words)
    output_diraction(output_file, diraction_list)


if __name__ == "__main__":
    """runs main"""
    main(sys.argv)
