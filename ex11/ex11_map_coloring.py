##############################################################
# FILE : ex11.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex11 2017-2018
# DESCRIPTION: coloring a map
#############################################################

from ex11_backtrack import general_backtracking
from time import time
#from map_coloring_gui import color_map #uncomment if you installed the required libraries

COLORS = ['red','blue','green','magenta','yellow','cyan']

### to implement
def read_adj_file(adjacency_file):
    """
    A countries dict from a txt file bilder
    :param adjacency_file:A file containing a list of countries with the
                           neighboring countries of each country
    :return: a dict for the file
    """
    countries = {}
    f_map = open(adjacency_file, "r")
    lines = f_map.read()
    line = lines.split("\n")
    for i in range(len(line)):
        if len(line[i]) > 1:
            row1 = line[i].split(":")
            row = row1[1].split(",")
            if row == ['']:
                countries[row1[0]] = ''
            else:
                countries[row1[0]] = row
    f_map.close()
    return countries


def num_colors_check(num_colors):
    """
    gets the colors from the list
    :param num_colors: the user selaction
    :return: a set of legal assignments
    """
    set_of_assignments = []
    for i in range(num_colors):
        set_of_assignments.append(COLORS[i])
    return set_of_assignments


def legal_assignment_func(dict_items_to_vals, list_of_items, countries):
    """

    :param dict_items_to_vals: a dict with a contry and its color
    :param list_of_items: a spesipic contry
    :param countries: a dict of all countrys and thir nighbers
    :return: true if the assignment is legal an false if its not
    """
    if countries[list_of_items] != None:
        neighbors = countries[list_of_items]
        for i in range(len(neighbors)):
            if dict_items_to_vals[neighbors[i]] == \
                    dict_items_to_vals[list_of_items]:
                return False
            else:
                continue
    return True

def run_map_coloring(adjacency_file, num_colors = 4, map_type = None):
    """

    :param adjacency_file: a txt file with contrys and thir nighbers
    :param num_colors:a selaction from the user
    :param map_type: the type of map we are useing
    :return: if there is a solotion it shows it and None if there is no
             solotion
    """
    countries = read_adj_file(adjacency_file)
    list_of_items = []
    for key in countries.keys():
        list_of_items.append(key)
    dict_items_to_vals = {}
    for key in countries.keys():
        dict_items_to_vals[key] = "color"
    if num_colors == 1:
        return None
    else:
        set_of_assignments = num_colors_check(num_colors)
        if general_backtracking(list_of_items, dict_items_to_vals, 0,
                                set_of_assignments, legal_assignment_func,
                                countries):

            return dict_items_to_vals
        else:
            return None
