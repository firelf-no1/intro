##############################################################
# FILE : ex11.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: coloring a map faster
#############################################################
import ex11_map_coloring
from ex11_backtrack import general_backtracking
# from map_coloring_gui import color_map #uncomment if you installed the required libraries

ADJ_DICT_LEN = 60
COLORS_LEN = 4

### to implement


def max_finder(adj_dict):
    """
    makes a list of the contrys from the one with the most neighbors
    :param adj_dict: dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :return: a list of the contreys with the max nighbors
    """
    byprey = sorted([(len(v), k) for k, v in adj_dict.items()],
                    reverse=True)
    max_neighbors = []
    for i in range(len(byprey)):
        max_neighbors.append(byprey[i][1])
    return max_neighbors


def back_track_degree_heuristic(adj_dict, colors):
    """
    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :return: The output of the helper_run_map_coloring function that returns
             True if possible paint all the country in a different color
             from all neighboring countries, and None if not.
    """
    dict_items_to_vals = {}
    for key in adj_dict.keys():
        dict_items_to_vals[key] = "color"
    max_list = max_finder(adj_dict)
    if general_backtracking(max_list, dict_items_to_vals, 0, colors,
                            ex11_map_coloring.legal_assignment_func, adj_dict):
        return dict_items_to_vals
    else:
        return None


def minimum_remaining_values(adj_dict, dict_items_to_vals, colors, key_list):
    """
    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param dict_items_to_vals: A dictionary whose keys are the names of the
                           countries and the values of each key are
                           neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :param key_list: the list of all the keys from the adj_dict
    :return: the list of keys with the lowest valve
    """
    vals_dict = list()
    for i in range(len(key_list)):
        if dict_items_to_vals[key_list[i]] not in colors:
            counter = 0
            num = dict_items_to_vals[key_list[i]]
            for color in colors:
                dict_items_to_vals[key_list[i]] = color
                if ex11_map_coloring.legal_assignment_func(dict_items_to_vals,
                                                           key_list[i],
                                                           adj_dict):
                    counter += 1
                else:
                    continue
            dict_items_to_vals[key_list[i]] = num
            vals_dict.append((counter, key_list[i]))
    list_min = sorted(vals_dict)
    min_list = list()
    for i in range(len(list_min)):
        min_list.append(list_min[i][1])
    return min_list


def list_update(min_list, dict_items_to_vals, index, colors,
                legal_assignment_func, adj_dict, key_list):
    """
    :param min_list: a list of keys with the lowest valve
    :param dict_items_to_vals: A dictionary whose keys are the names of the
                           countries and the values of each key are
                           neighboring of the country.
    :param index: the index we are working on
    :param colors: List of colors that are allowed to paint the countries
    :param legal_assignment_func:
    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param key_list: the list of all the keys from the adj_dict
    :return: true or false for the loop
    """
    if len(min_list) == 0:
        return True
    if dict_items_to_vals[min_list[index]] not in colors:
        for color in colors:
            num = dict_items_to_vals[min_list[index]]
            dict_items_to_vals[min_list[index]] = str(color)
            if legal_assignment_func(dict_items_to_vals, min_list[index],
                                     adj_dict):
                min_list1 = minimum_remaining_values(adj_dict,
                                                    dict_items_to_vals, colors,
                                                    key_list)
                if list_update(min_list1, dict_items_to_vals, 0, colors,
                            legal_assignment_func, adj_dict,
                               key_list):
                    return True
                else:
                    dict_items_to_vals[min_list[index]] = str(num)
                    continue
            else:
                dict_items_to_vals[min_list[index]] = str(num)
        return False


def back_track_MRV(adj_dict, colors):
    """
    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :return: True if possible paint all the country in a different color
             from all neighboring countries (In this case, a dictionary will
             also be printed with the color of each country), and None if not.
    """
    dict_items_to_vals = {}
    key_list = list()
    for key in adj_dict.keys():
        dict_items_to_vals[key] = "color"
        key_list.append(key)
    min_list = minimum_remaining_values(adj_dict, dict_items_to_vals, colors,
                                        key_list)
    if list_update(min_list, dict_items_to_vals, 0, colors,
                   ex11_map_coloring.legal_assignment_func, adj_dict,
                   key_list):
        return dict_items_to_vals
    else:
        return None


def minimum_remaining_colors(adj_dict, dict_items_to_vals, colors, key_list):
    """

    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param dict_items_to_vals: A dictionary whose keys are the names of the
                           countries and the values of each key are
                           neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :param key_list: the list of all the keys from the adj_dict
    :return:
    """
    for i in range(len(key_list)):
        if dict_items_to_vals[key_list[i]] not in colors:
            counter = []
            num = dict_items_to_vals[key_list[i]]
            for color in colors:
                dict_items_to_vals[key_list[i]] = color
                if ex11_map_coloring.legal_assignment_func(dict_items_to_vals,
                                                           key_list[i],
                                                           adj_dict):
                    counter.append(color)
                else:
                    continue
            dict_items_to_vals[key_list[i]] = num
            if counter == []:
                return False
    return True


def fc_loop(dict_items_to_vals, index, colors,
                   legal_assignment_func, adj_dict):
    """

    :param dict_items_to_vals: A dictionary whose keys are the names of the
                           countries and the values of each key are
                           neighboring of the country.
    :param index: the index we are working on
    :param colors: List of colors that are allowed to paint the countries
    :param legal_assignment_func:
    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :return: true or fulse for the map criation
    """
    max_list = max_finder(adj_dict)
    if index == len(max_list):
        return True
    for color in colors:
        num = dict_items_to_vals[max_list[index]]
        if dict_items_to_vals[max_list[index]] not in colors:
            dict_items_to_vals[max_list[index]] = color
            if legal_assignment_func(dict_items_to_vals, max_list[index],
                                     adj_dict):
                if minimum_remaining_colors(adj_dict, dict_items_to_vals,
                                            colors, max_list):
                    if fc_loop(dict_items_to_vals, index + 1, colors,
                               legal_assignment_func, adj_dict):
                        return True
                    else:
                        dict_items_to_vals[max_list[index]] = num
                        continue
                else:
                    dict_items_to_vals[max_list[index]] = num
                    continue
            else:
                dict_items_to_vals[max_list[index]] = num
                continue
        else:
            continue
    return False


def back_track_FC(adj_dict, colors):
    """

    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :return:
    """
    dict_items_to_vals = {}
    for key in adj_dict.keys():
        dict_items_to_vals[key] = "color"
    if fc_loop(dict_items_to_vals, 0, colors,
                   ex11_map_coloring.legal_assignment_func, adj_dict):
        return dict_items_to_vals
    else:
        return None


def color_counter(adj_dict, colors, dict_items_to_vals, index):
    """

    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :param dict_items_to_vals: A dictionary whose keys are the names of the
                           countries and the values of each key are
                           neighboring of the country.
    :param index: the index we are working on
    :return:
    """
    max_num_legal_colors = 0
    max_color = ''
    neighbors = adj_dict[index]
    num_legal_colors = 0
    for neighbor_color in colors:
        for neighbor in neighbors:
            old_num = dict_items_to_vals[neighbor]
            dict_items_to_vals[neighbor] = neighbor_color
            if ex11_map_coloring.legal_assignment_func(
                    dict_items_to_vals, index, adj_dict):
                num_legal_colors += 1
            else:
                dict_items_to_vals[neighbor] = old_num
        if num_legal_colors > max_num_legal_colors:
            max_num_legal_colors = num_legal_colors
            max_color = dict_items_to_vals[index]
    if max_color == '':
        return None
    return max_color


def back_track_LCV(adj_dict, colors):
    """
    :param adj_dict: A dictionary whose keys are the names of the countries
                     and the values of each key are neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :return:  True if possible paint all the country in a different color
              from all neighboring countries, and None if not
    """
    max_list = max_finder(adj_dict)
    dict_items_to_vals = {}
    for key in adj_dict.keys():
        dict_items_to_vals[key] = 'color'
    if lcv_loop(max_list, dict_items_to_vals, 0, colors, adj_dict):
        return dict_items_to_vals
    else:
        return None


def lcv_loop(max_list, dict_items_to_vals, index, colors, adj_dict):
    """
    :param max_list: List of all countries we want to paint
    :param dict_items_to_vals: A dictionary whose keys are names of countries
                           and the value of each country is a color or "color"
    :param index: A number (int) indicating the position in countries_list
                 of the item we are trying to paint at this time of recursion
    :param colors: List of colors that are allowed to paint the countries
    :param adj_dict: A dictionary whose keys are the names of the
                           countries and the values of each key are
                           neighboring of the country.
    :return: A dictionary whose keys are the names of the countries
             and the values of each key are neighboring of the country
    """
    if index == len(max_list):
        return True
    else:
        num = dict_items_to_vals[max_list[index]]
        if adj_dict[max_list[index]] != None:
            old_colors = colors
            for color in old_colors:
                dict_items_to_vals[max_list[index]] = color
                if ex11_map_coloring.legal_assignment_func(dict_items_to_vals,
                                                           max_list[index],
                                                           adj_dict):
                    new_color = color_counter(adj_dict, old_colors,
                                              dict_items_to_vals,
                                          max_list[index])
                    if new_color != None:
                        dict_items_to_vals[max_list[index]] = new_color
                        if lcv_loop(max_list, dict_items_to_vals,
                                                index + 1, colors, adj_dict):
                            return True
                        else:
                            dict_items_to_vals[max_list[index]] = num
                            if new_color not in old_colors:
                                lcv_loop(max_list, dict_items_to_vals,
                                index, colors, adj_dict)
                            else:
                                old_colors.remove(new_color)
                                lcv_loop(max_list, dict_items_to_vals,
                                         index, old_colors, adj_dict)
        else:
            dict_items_to_vals[max_list[index]] = colors[0]
            if lcv_loop(max_list, dict_items_to_vals,
                                     index + 1, colors, adj_dict):
                return True
    return False


def fast_back_track(adj_dict, colors):
    """
    :param adj_dict:  dictionary whose keys are the names of the countries
                    and the values of each key are neighboring of the country.
    :param colors: List of colors that are allowed to paint the countries
    :return: if its true return the map if its false returns none
    """
    if len(adj_dict) <= ADJ_DICT_LEN:
        return back_track_degree_heuristic(adj_dict, colors)
    elif len(adj_dict) > ADJ_DICT_LEN and len(colors) > COLORS_LEN:
        return back_track_degree_heuristic(adj_dict, colors)
    elif len(adj_dict) > ADJ_DICT_LEN and len(colors) <= COLORS_LEN:
        return back_track_MRV(adj_dict, colors)



