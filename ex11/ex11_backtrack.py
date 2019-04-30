
import math

def general_backtracking(list_of_items, dict_items_to_vals, index,
                    set_of_assignments, legal_assignment_func,
                    *args):
    """
    a general back tracking helper
    :param list_of_items: A list of the items that we would like to assign.
    :param dict_items_to_vals: A dictionary containing keys from
           items_of_list  and assignment values from set_of_assignments.
    :param index: A number (int) indicating the position in the item_of_list
           of the item we are trying to update at this time of recursion.
    :param set_of_assignments: A set of values that are valid as values in
           the dictionary.
    :param legal_assignment_func: Pointer for a specific function that
           checks the integrity of one assign
    :param args: A list of additional variables that can be passed to the
           function
    :return: assign all the items from set list_of_items into the
             dictionary (as keys) with values from set_of_assignments (as
             values) so that all of them are valid according to the
             legal_assignment_func
    """
    if index == len(list_of_items):
        return True
    if dict_items_to_vals[list_of_items[index]] not in set_of_assignments:
        for assignment in set_of_assignments:
            num = dict_items_to_vals[list_of_items[index]]
            dict_items_to_vals[list_of_items[index]] = assignment
            if legal_assignment_func(dict_items_to_vals, list_of_items[index],
                                     *args):
                if general_backtracking(list_of_items, dict_items_to_vals,
                                     index + 1, set_of_assignments,
                                     legal_assignment_func, *args):
                    return True
            dict_items_to_vals[list_of_items[index]] = num
    return False


