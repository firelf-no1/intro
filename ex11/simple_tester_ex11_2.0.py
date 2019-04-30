import ex11_sudoku as sudoku
import ex11_map_coloring as map_colors
import ex11_improve_backtrack as improved
import time

map_module = False
try:
    from map_coloring_gui import color_map
    map_module = True
except ImportError:
    pass


COLORS = ['red', 'blue', 'green', 'magenta', 'yellow', 'cyan']

ADJ_FILES = ['adjacency_files/adj_usa_ex11.txt',
             'adjacency_files/adj_world_ex11.txt']
ADJ_US = map_colors.read_adj_file(ADJ_FILES[0])
ADJ_WORLD = map_colors.read_adj_file(ADJ_FILES[1])

ADJ_DICTS = [ADJ_US, ADJ_WORLD]
SUDOKU_BOARDS = ['sudoku_tables/sudoku_table1.txt',
                 'sudoku_tables/sudoku_table2.txt',
                 'sudoku_tables/sudoku_table3.txt']


def get_num_colors():
    return int(input('How many colors? (Enter a number 0-6)'))


def get_map():
    return int(input('Which map? (US map = 0 World map = 1)'))


def get_num_algorithm():
    return int(input('How many algorithms to check? (Enter a number 1-6)'))


def timer(start):
    return float(time.clock()) - float(start)


def result_check(result, map_type):
    if result:
        print('Found solution')
        if truth_test(ADJ_DICTS[map_type], result):
            print('Solution is correct', )
        else:
            print('Solution is not legal!', )
    else:
        print('No solution')


# Tip: to print all docstrings to file, use terminal command: pydoc -w ./<*>.py
def tester(sudoku_test=False, maps_test=False):

    print('Starting Tests:')
    # if maps_test:
    num_colors = get_num_colors()
    map_type = get_map()
    # algorithms = get_num_algorithm()

    start_time = time.clock()
    if sudoku_test:
        sudoku_tests()
    if maps_test:
        maps_tester(num_colors, map_type)
        # maps_tester()

    print('\n\nTotal Runtime:', float(time.clock()) - float(start_time))


def sudoku_tests():
    start_time = time.clock()
    print('\nSudoku 1 test:')
    if sudoku.run_game(SUDOKU_BOARDS[0], True):
        print('Sudoku 1 passed')
    else:
        print('Sudoku 1 - Failed - No solution')
    print('Runtime:', timer(start_time))

    start_time2 = time.clock()
    print('\nSudoku 2 test:')
    if sudoku.run_game(SUDOKU_BOARDS[1], True):
        print('Sudoku 2 passed')
    else:
        print('Sudoku 2 - Failed - No solution')
    print('Runtime Sudoku 2:', timer(start_time2))

    start_time3 = time.clock()
    print('\nSudoku 3 test:')
    if not sudoku.run_game(SUDOKU_BOARDS[2], True):
        print('Sudoku 3 no solution as expected - Passed')
    else:
        print('Sudoku 3 failed- Should be no solution')
    print('Runtime Sudoku 3:', timer(start_time3))


def maps_tester(num_colors=4, map_type=0, algorithms=5):
    if map_module:
        if map_type == 0:
            map_str = 'USA'
        else:
            map_str = 'world'
    else:
        map_str = None
    print('\n\nTesting Map coloring - General Backtracking:')

    start_time_map = time.clock()
    result1 = map_colors.run_map_coloring(ADJ_FILES[map_type],
                                         num_colors, map_str)
    runtime_bt = timer(start_time_map)
    result_check(result1, map_type)
    # color_map(result, map_str)
    print('Runtime:', runtime_bt)

    if algorithms > 1:
        start_time_degree = time.clock()
        print('\n\nNow Testing map coloring - Degree Heuristic:')
        result2 = improved.back_track_degree_heuristic(ADJ_DICTS[map_type],
                                                      COLORS[:num_colors])
        runtimeDH = timer(start_time_degree)
        result_check(result2, map_type)
        print('Runtime DH:', runtimeDH)
        print('DH is', str(runtime_bt / runtimeDH),
              'times faster than general BT.')

    if algorithms > 2:
        start_time_mrv = time.clock()
        print('\n\nNow Testing map coloring - MRV:')
        result3 = improved.back_track_MRV(ADJ_DICTS[map_type],
                                         COLORS[:num_colors])
        runtimeMRV = timer(start_time_mrv)
        result_check(result3, map_type)
        print('Runtime MRV:', runtimeMRV)
        print('MRV is', str(runtime_bt / runtimeMRV),
              'times faster than general BT.')

    if algorithms > 3:
        start_time_FC = time.clock()
        print('\n\nNow Testing map coloring - FC:')
        result4 = improved.back_track_FC(ADJ_DICTS[map_type],
                                        COLORS[:num_colors])
        runtimeFC = timer(start_time_FC)
        result_check(result4, map_type)
        print('Runtime FC:', runtimeFC)
        print('FC is', str(runtime_bt / runtimeFC),
              'times faster than general BT.')

    if algorithms > 4:
        start_time_LCV = time.clock()
        print('\n\nNow Testing map coloring - LCV:')
        result5 = improved.back_track_LCV(ADJ_DICTS[map_type],
                                         COLORS[:num_colors])
        runtimeLCV = timer(start_time_LCV)
        result_check(result5, map_type)
        print('Runtime LCV:', runtimeLCV)
        print('LCV is', str(runtime_bt / runtimeLCV),
              'times faster than general BT.')

    if algorithms > 5:
        start_time_Fast = time.clock()
        print('\n\nNow Testing map coloring - Fast:')
        result6 = improved.fast_back_track(ADJ_DICTS[map_type],
                                          COLORS[:num_colors])
        runtimeFast = timer(start_time_Fast)
        result_check(result6, map_type)
        print('Runtime Fast:', runtimeFast)
        print('Fast is', str(runtime_bt / runtimeFast),
              'times faster than general BT.')

    if map_module:
        color_map(result1, map_str)
        color_map(result2, map_str)
        color_map(result3, map_str)
        color_map(result4, map_str)
        color_map(result5, map_str)
        color_map(result6, map_str)
        # except:
        #     print("Couldn't load map module")


def truth_test(adj_dict, result):
    for k, v in result.items():
        for i in adj_dict[k]:
            if v == result[i]:
                return False
    return True


if __name__ == "__main__":
    tester(True, True)
