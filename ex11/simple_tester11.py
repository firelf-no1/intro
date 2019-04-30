import ex11_sudoku as sudoku
import ex11_map_coloring as map_colors
import ex11_improve_backtrack as improved
import time

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
    return float(time.time()) - float(start)


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
def tester(sudoku_test=False, maps_test=False, num_colors=6, map_type=0,
           algorithms=1):
    print('Starting Tests:')
    start_time = time.time()

    if sudoku_test:
        print('\nSudoku 1 test:')
        if sudoku.run_game(SUDOKU_BOARDS[0], True):
            print('Sudoku 1 passed')
        else:
            print('Sudoku 1 - Failed - No solution')
        print('Runtime:', timer(start_time))

        start_time2 = time.time()
        print('\nSudoku 2 test:')
        if sudoku.run_game(SUDOKU_BOARDS[1], True):
            print('Sudoku 2 passed')
        else:
            print('Sudoku 2 - Failed - No solution')
        print('Runtime Sudoku 2:', timer(start_time2))

        start_time3 = time.time()
        print('\nSudoku 3 test:')
        if not sudoku.run_game(SUDOKU_BOARDS[2], True):
            print('Sudoku 3 no solution as expected - Passed')
        else:
            print('Sudoku 3 failed- Should be no solution')
        print('Runtime Sudoku 3:', timer(start_time3))

    if maps_test:
        print('\n\nTesting Map coloring - General Backtracking:')

        start_time_map = time.time()
        result = map_colors.run_map_coloring(ADJ_FILES[map_type],
                                             num_colors)
        runtime_bt = timer(start_time_map)
        result_check(result, map_type)
        print('Runtime:', runtime_bt)

        if algorithms > 1:
            start_time_degree = time.time()
            print('\n\nNow Testing map coloring - Degree Heuristic:')
            result = improved.back_track_degree_heuristic(ADJ_DICTS[map_type],
                                                          COLORS[:num_colors])
            runtimeDH = timer(start_time_degree)
            result_check(result, map_type)
            print('Runtime DH:', runtimeDH)
            print('DH is', str(runtime_bt / runtimeDH),
                  'times faster than general BT.')

        if algorithms > 2:
            start_time_mrv = time.time()
            print('\n\nNow Testing map coloring - MRV:')
            result = improved.back_track_MRV(ADJ_DICTS[map_type],
                                             COLORS[:num_colors])
            runtimeMRV = timer(start_time_mrv)
            result_check(result, map_type)
            print('Runtime MRV:', runtimeMRV)
            print('MRV is', str(runtime_bt / runtimeMRV),
                  'times faster than general BT.')

        if algorithms > 3:
            start_time_FC = time.time()
            print('\n\nNow Testing map coloring - FC:')
            result = improved.back_track_FC(ADJ_DICTS[map_type],
                                            COLORS[:num_colors])
            runtimeFC = timer(start_time_FC)
            result_check(result, map_type)
            print('Runtime FC:', runtimeFC)
            print('FC is', str(runtime_bt / runtimeFC),
                  'times faster than general BT.')

        if algorithms > 4:
            start_time_LCV = time.time()
            print('\n\nNow Testing map coloring - LCV:')
            result = improved.back_track_LCV(ADJ_DICTS[map_type],
                                             COLORS[:num_colors])
            runtimeLCV = timer(start_time_LCV)
            result_check(result, map_type)
            print('Runtime LCV:', runtimeLCV)
            print('LCV is', str(runtime_bt / runtimeLCV),
                  'times faster than general BT.')

        if algorithms > 5:
            start_time_Fast = time.time()
            print('\n\nNow Testing map coloring - Fast:')
            result = improved.fast_back_track(ADJ_DICTS[map_type],
                                              COLORS[:num_colors])
            runtimeFast = timer(start_time_Fast)
            result_check(result, map_type)
            print('Runtime Fast:', runtimeFast)
            print('Fast is', str(runtime_bt / runtimeFast),
                  'times faster than general BT.')

    print('\n\nTotal Runtime:', float(time.time()) - float(start_time))


def truth_test(adj_dict, result):
    for k, v in result.items():
        for i in adj_dict[k]:
            if v == result[i]:
                print(v, result[i])
                return False
    return True


if __name__ == "__main__":
    tester(True, True, get_num_colors(), get_map(), get_num_algorithm())
