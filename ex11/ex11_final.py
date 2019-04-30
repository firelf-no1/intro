import zipfile
import os
import tempfile
import sys
import traceback
import timeit
import copy

MAX_POINTS = 50
README_MISSING_REDUCTION = 5
MINOR_TEST_FAIL_REDUCTION = 3
BIG_TEST_FAIL_REDUCTION = 8

sys.path.append("/cs/course/2017/intro2cs/bin/final/classes")
sys.path.append("/cs/course/2017/intro2cs/bin/final/classes/ex10_data/")

SUDOKU_FILES_DIR = '/cs/course/2017/intro2cs/bin/final/ex11_final/ex11_files/sudoku_tables/'
ADJACENCY_FILES_FIR = '/cs/course/2017/intro2cs/bin/final/ex11_final/ex11_files/adjacency_files/'


import Timeout2


class StdOutToList:
    def __init__(self):
        self.data = []

    def write(self, s):
        self.data.append(s)

    def __enter__(self):
        sys.stdout = self
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.stdout = sys.__stdout__
        self.flush()

    def flush(self):
        self.data = []


def write_grade(grade,time,bonus):
    password = 15467984
    print("\nYour final grade in the autotest is: " + str(
        grade) + " out of 50.\n")
    result_fd = os.fdopen(3, "w")
    result_fd.write("Passwaord:" + str(password) + "\n")
    result_fd.write(str(grade) + "," + str(time) + "," + str(bonus) )
    sys.exit()


print(
    "                                    .-'''-.                        _..._               \n                                   '   _    \      .-''-.       .-'_..._''.            \n.--.   _..._                     /   /` '.   \   .' .-.  )    .' .'      '.\           \n|__| .'     '.                  .   |     \  '  / .'  / /    / .'                      \n.--..   .-.   .     .|  .-,.--. |   '      |  '(_/   / /    . '                        \n|  ||  '   '  |   .' |_ |  .-. |\    \     / /      / /     | |                        \n|  ||  |   |  | .'     || |  | | `.   ` ..' /      / /      | |                   _    \n|  ||  |   |  |'--.  .-'| |  | |    '-...-'`      . '       . '                 .' |   \n|  ||  |   |  |   |  |  | |  '-                  / /    _.-')\ '.          .   .   | / \n|__||  |   |  |   |  |  | |                    .' '  _.'.-''  '. `._____.-'/ .'.'| |// \n    |  |   |  |   |  '.'| |                   /  /.-'_.'        `-.______ /.'.'.-'  /  \n    |  |   |  |   |   / |_|                  /    _.'                    ` .'   \_.'   \n    '--'   '--'   `'-'                      ( _.-'                                     \n\n\n")

# make the temp dir
tmp_dir = tempfile.mkdtemp()

# unzip the files
if len(sys.argv) <= 1:
    print("no argument supllied")
    exit()

zip_ref = zipfile.ZipFile(sys.argv[1], 'r')
zip_ref.extractall(tmp_dir)
zip_ref.close()

total_points = MAX_POINTS

if (os.path.isfile(tmp_dir + "//README") and \
        os.stat(tmp_dir + "//README").st_size != 0):  # file included
    # The READMY exist
    print("The README was tested and found Okay")
else:
    print("The README file doesn't exist or is empty.\n 5 points were reduced")
    total_points = total_points - README_MISSING_REDUCTION

# adds the tmp_dir to path
sys.path.append(tmp_dir)
sdtout_original = sys.stdout
stdin_original = sys.stdin

#######################################################
# test names
names = { 'ex11_backtrack' : {'general_backtracking'} \
    , 'ex11_sudoku' : {'run_game'} \
    , 'ex11_map_coloring' : {'run_map_coloring'} \
          }
try:
    for file_name in names.keys():
        if (os.path.isfile(tmp_dir + "//" + file_name + ".py") and \
                os.stat(tmp_dir + "//" + file_name + ".py").st_size != 0):
            # the file file_name exists
            with Timeout2.Timeout(2):
                temp_stdout = StdOutToList()
                with temp_stdout:
                    try:
                        exec("import " + file_name)
                    except:
                        sys.stdout = sdtout_original
                        print(file_name + " import raised an exception." + "\nAll points of the autotest were reduced ")
                        traceback.print_exc()
                        write_grade(0)
            for function_name in names[file_name]:
                # check if function_name exist in file_name
                if not (function_name in dir(eval(file_name))):
                    print(
                        "function " + function_name + " is missing from " + file_name + ".\nAll points of the autotest were reduced ")
                    write_grade(0)
        else:
            print("The file " + file_name + ".py is missing.\nAll points of the autotest were reduced ")
            write_grade(0,-1,false)
except Exception as e:
    print("Name test has raised an exception:")
    print(e)
    print("All points of the autotest were reduced")
    write_grade(0,-1,false)

#######################################################
print("Testing ex11_sudoku file\n")
try:
    with Timeout2.Timeout(1):
        import ex11_sudoku
except:
    print("ex11_sudoku import raised an exception." + "\nAll points of the autotest were reduced ")
    write_grade(0,-1,false)



sudoku_files_list = ['sudoku_table4.txt','sudoku_table5.txt','sudoku_table6.txt']
expected_result = [True, True, False]

for i in range(len(sudoku_files_list)):
    sudoku = sudoku_files_list[i]
    expected = expected_result[i]
    print("Running ex11_sudoku with "+sudoku+".  ---> ", end="")
    try:
        with Timeout2.Timeout(420):
            student_result = ex11_sudoku.run_game(SUDOKU_FILES_DIR + sudoku)
        if isinstance(student_result, bool) and student_result == expected:
            print("test passed!\n")
        else:
            print('test failed...')
            print('expected: '+str(expected)+'. but got '+str(student_result))
            print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
            total_points = total_points - BIG_TEST_FAIL_REDUCTION
    except Exception as e:
        print("your code raised and exception: ")
        print(e)
        print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
        total_points = total_points - BIG_TEST_FAIL_REDUCTION

#####################################################
print("Testing ex11_backtrack file\n")
try:
    with Timeout2.Timeout(1):
        import ex11_backtrack
except:
    print("ex11_backtrack import raised an exception." + "\nAll points of the autotest were reduced ")
    write_grade(0,-1,false)


def make_queen_list(number_of_queens):
    queen_list = []
    for i in range(number_of_queens):
        queen = 'queen_'+str(i)
        queen_list.append(queen)
    return queen_list

def make_starting_queen_dict(queens_list):
    queens_dict = {}
    for queen in queens_list:
        queens_dict[queen] = None
    return queens_dict

def make_board(board_size):
    board = {}
    for i in range(board_size):
        for j in range(board_size):
            board[(i, j)] = 0
    return board


def is_location_safe(queens_dict, queen_to_check, *args):
    # first trying to get the right args in the right place
    true_queen = queen_to_check
    true_dict = queens_dict
    if not isinstance(queens_dict, dict):
        true_queen = queens_dict
        true_dict = queen_to_check

    location_to_check = true_dict[true_queen]

    printf = True

    location_x = location_to_check[0]
    location_y = location_to_check[1]

    for queen in true_dict:
        queen_location = true_dict[queen]
        if queen_location is None or queen == queen_to_check:
            continue
        queen_x, queen_y = queen_location
        # check row and col
        if queen_x == location_x or queen_y == location_y:
            return False
        # check diagonally for +-8 steps from queen, will not make the board bigger
        for i in range(1, 8):
            if queen_x+i == location_x and queen_y+i == location_y or queen_x-i == location_x and queen_y-i == location_y:
                return False
        # check other diagonal
        for i in range(1, 8):
            if queen_x+i == location_x and queen_y-i == location_y or queen_x-i == location_x and queen_y+i == location_y:
                return False
    for queen in true_dict:
        if true_dict[queen] is None:
            printf = False
    if printf:
        print('Your solution is : ', end='')
        print(true_dict)
    return True


print("For the mystery problem :\n"
      "your general backtracking algorithm will try"
      "to solve the \"Eight queens puzzle\".\n"
      "We will also check the problem with 4 queens and a 4x4 board.\n"
      "And 3 queens on a 3x3 board, which has no solution.\n")
print("For more information on the Eight queens puzzle :")
print("https://en.wikipedia.org/wiki/Eight_queens_puzzle\n")


number_of_queens_list = [8, 4, 3]
expected_result = [True, True, False]

for i in range(len(number_of_queens_list)):
    number_of_queens = number_of_queens_list[i]
    expected = expected_result[i]
    print('Running the '+str(number_of_queens)+' queens problem   ---->   ', end='')
    try:
        queens = make_queen_list(number_of_queens)
        stating_dict = make_starting_queen_dict(queens)
        board = make_board(number_of_queens)
        with Timeout2.Timeout(420):
            student_result = ex11_backtrack.general_backtracking(queens, stating_dict, 0, board, is_location_safe)
        if isinstance(student_result, bool) and student_result == expected:
            print("test passed!\n")
        else:
            print('test failed...')
            print('expected: '+str(expected)+'. but got ' + str(student_result))
            print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
            total_points = total_points - BIG_TEST_FAIL_REDUCTION
    except Exception as e:
        print("your code raised and exception: ")
        print(e)
        traceback.print_exc()
        print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
        total_points = total_points - BIG_TEST_FAIL_REDUCTION


#####################################################
print("Testing ex11_map_coloring file\n")
try:
    with Timeout2.Timeout(1):
        import ex11_map_coloring
except:
    print("ex11_map_coloring import raised an exception." + "\nAll points of the autotest were reduced ")
    write_grade(0,-1,false)


def is_valid_solution(solution_dict, adjacency_dict):
    for country, country_color in solution_dict.items():
        neighbors = adjacency_dict[country]
        for neighbor in neighbors:
            if solution_dict[neighbor] == country_color:
                return False, country, neighbor
    return True, None, None


def read_adj_mat(filename):
    adj_mat = {}
    with open(filename) as adj_file:
        for line in adj_file:
            st1 = line.strip().split(":")
            if len(st1[1]) == 0:
                adj_mat[st1[0]] = []
            else:
                ne = st1[1].split(",")
                adj_mat[st1[0]] = ne

    return adj_mat


adj_files_list = ['adj_usa_mod_ex11.txt', 'adj_usa_ex11.txt']
for i in range(len(adj_files_list)):
    try:
        adj_file_name = adj_files_list[i]
        print('Running \"run_map_coloring\" with \"'+adj_file_name+'\"')
        adj_file = ADJACENCY_FILES_FIR + adj_file_name
        with Timeout2.Timeout(1360):
            student_sol = ex11_map_coloring.run_map_coloring(adj_file)
        if student_sol:
            passed, problem_country1, problem_country2 = is_valid_solution(student_sol, read_adj_mat(adj_file))
            if passed:
                print("test passed!\n")
            else:
                print('test failed...')
                print('country '+problem_country1+' and '+problem_country2+' has the same color')
                print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
                total_points = total_points - BIG_TEST_FAIL_REDUCTION
        else:
            print('test failed...')
            print('got None while there is a solution')
            print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
            total_points = total_points - BIG_TEST_FAIL_REDUCTION
    except Exception as e:
        print("your code raised and exception: ")
        print(e)
        traceback.print_exc()
        print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
        total_points = total_points - BIG_TEST_FAIL_REDUCTION

## just 1 color, no solution
try:
    print('Running \"run_map_coloring\" with \"adj_usa_ex11.txt\" and 1 color')
    adj_file = ADJACENCY_FILES_FIR + 'adj_usa_ex11.txt'
    with Timeout2.Timeout(1360):
        student_sol = ex11_map_coloring.run_map_coloring(adj_file, num_colors=1)
    if student_sol is None:
        print("test passed!\n")
    else:
        print('test failed...')
        print('Expected None')
        print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
        total_points = total_points - BIG_TEST_FAIL_REDUCTION
except Exception as e:
    print("your code raised and exception: ")
    print(e)
    traceback.print_exc()
    print(str(BIG_TEST_FAIL_REDUCTION) + " points were reduced\n")
    total_points = total_points - BIG_TEST_FAIL_REDUCTION

#####################################################
print("Bonus Round!!!\n")
bonus = True
bonus_time = 3000
try:
    with Timeout2.Timeout(1):
        import ex11_improve_backtrack
except:
    print("ex11_improve_backtrack import failed." + "\n no bonus tests")
    bonus = False

print('All below functions are timed with the \"timeit\" module')

## checking 4 and 3 colors
tamriel_dict = read_adj_mat(ADJACENCY_FILES_FIR + 'tamriel_adj_ex11.txt')

if bonus:
    bonus_time = 0
    dict_list = [tamriel_dict, tamriel_dict]
    colors_list = [['red', 'blue', 'green', 'yellow'], ['red', 'blue', 'green']]
    for i in range(len(dict_list)):
        dict_to_check = copy.deepcopy(dict_list[i])
        colors = colors_list[i]
        print('Running \"fast_back_track\" with a dictionary from tamriel_adj_ex11.txt and the colors :',colors)
        try:
            with Timeout2.Timeout(600):
                student_sol = ex11_improve_backtrack.fast_back_track(dict_to_check,colors)
                if student_sol:
                    if is_valid_solution(ex11_improve_backtrack.fast_back_track(dict_to_check,colors), dict_to_check):
                        time_f = timeit.timeit("ex11_improve_backtrack.fast_back_track(dict_to_check,colors)", globals=globals())
                        print('Your time :', time_f,'\n')
                        bonus_time += time_f
                    else:
                        print("Wrong solution, bonus failed \n")
                        bonus_time += 30000
                else:
                    print('Bonus failed')
                    print('got None while there is a valid solution\n')
                    bonus_time += 30000
        except Exception as e:
            print('Your code has raised an exception, Bonus failed\n')
            traceback.print_exc()
            bonus_time += 30000

## checking 2 and 1 colors , no soultion

    dict_list = [tamriel_dict, tamriel_dict]
    colors_list = [['red', 'blue'], ['red']]
    for i in range(len(dict_list)):
        dict_to_check = copy.deepcopy(dict_list[i])
        colors = colors_list[i]
        print('Running \"fast_back_track\" with a dictionary from tamriel_adj_ex11.txt and the colors :',colors)
        try:
            with Timeout2.Timeout(600):
                if ex11_improve_backtrack.fast_back_track(dict_to_check,colors) is None:
                    time_f = timeit.timeit("ex11_improve_backtrack.fast_back_track(dict_to_check,colors)", globals=globals())
                    print('Your time :', time_f,'\n')
                    bonus_time += time_f
                else:
                    print("Wrong solution, bonus failed \n")
                    bonus_time += 30000
        except Exception as e:
            print('Your code has raised an exception, Bonus failed')
            traceback.print_exc()
            bonus_time += 30000
    print('Your final time is : ', bonus_time)


#############################################################
sys.stdout = sys.__stdout__
sys.stdin = stdin_original
del ex11_sudoku
print("tests are done\n--------------------------\n")
#########################################
if (total_points > 0):
    write_grade(total_points,bonus_time,bonus)
else:
    write_grade(0,bonus_time,bonus)

