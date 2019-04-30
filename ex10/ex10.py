#File:ex10.py
#WRITER: itai shopen
#EXERCISE: intro2cs ex10 2017-2018
#DESCRIPTION: In this exercise I practiced using Decision Tree
import copy
import itertools
MAX_ERROR_RATE = 1


class Node:
    def __init__(self, data="", pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def is_leaf(self):
        #Checks if a particular node is a leaf
        if not self.positive_child:
            return False
        else:
            return True

    def get_positive_child(self):
            return self.positive_child

    def get_negative_child(self):
            return self.negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms

    def get_illness(self):
        return self.illness

    def get_symptoms(self):
        return self.symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.__root = root

    def diagnose(self, symptoms):
        """
        This function uses the root of the self-saved decision tree,
        receives a list of symptoms, and returns an illness that is
        on a leaf whose path corresponds to the symptoms
        """
        return self.diagnose_helper(self.__root, symptoms)

    def diagnose_helper(self, child, symptoms):
        """
        Recursive function that progresses towards a specific leaf
        according to the presence/absence of symptoms in the symptom list
        """
        if not child.is_leaf():
            # We reached the leaf - the end of the recursion
            return child.get_data()
        else:
            if child.get_data() in symptoms:
            # The symptom that is being asked is found in the list of symptoms
                return self.diagnose_helper(child.positive_child, symptoms)
            else: #is not found...
                return self.diagnose_helper(child.negative_child, symptoms)

    def calculate_error_rate(self, records):
        """
        This function receives a list of records and returns the ratio
        between the number of errors (discrepancy between the disease listed
        in the record and the disease that the function "diagnose" returns
        for the list of symptoms of the record) and the number of records
        """
        count_errors = 0 # Counts the number of errors
        for record in records:
            if self.diagnose(record.get_symptoms()) != record.get_illness():
                # Discrepancy
                count_errors += 1
        return count_errors / len(records)

    def all_illnesses(self):
        """
        This function uses the root of the self-saved decision tree,
        and return a list of all the illnesses that are stored on the tree
        leaves
        """
        return self.all_illnesses_helper([], self.__root)

    def all_illnesses_helper(self, illnesses_list, child):
        """
        A recursive function that passes through all the paths
        to all the leaves in the tree
        """
        if not child.is_leaf():
            if child.get_data() not in illnesses_list:
                """
                When we reach to a leaf, we will add the illness that is 
                reserved to the illnesses list
                """
                illnesses_list.append(child.get_data())
            return
        else:
            # For each symptom, we will check whether it exists or not
            self.all_illnesses_helper(illnesses_list, child.negative_child)
            self.all_illnesses_helper(illnesses_list, child.positive_child)
            return sorted(illnesses_list)

    def most_common_illness(self, records):
        """
        This function receives a list of records and returns the illness
        that function diagnose will return most often for the symptom
        lists in the records
        """
        illness_dict = {}
        """
        In each dictionary cell, the function saves the received illness 
        as a key and the number of times received as a value
        """
        for record in records:
            illness = self.diagnose(record.symptoms)
            illness_dict = self.add_illness_to_dict(illness_dict, illness)
        return self.most_common_illness_from_dict(illness_dict)


    def add_illness_to_dict(self, illness_dict, illness):
        """
        This function receives a dictionary and a illness. if the illness is
        in the dictionary, the function will add 1 to its value, else,
        it add to its value 1. The function returns the updated dictionary
        """
        if illness in illness_dict:
            illness_dict[illness] += 1
        else:
            illness_dict[illness] = 1
        return illness_dict


    def most_common_illness_from_dict(self, illness_dict):
        """
        This function receives a dictionary. In each cell,
        the key is the name of a illness and the value is a number. The
        function will return the name of the illness with the highest value
        """
        biggest, common_illness = 0, ""
        for illness in illness_dict:
            if illness_dict[illness] > biggest:
                biggest = illness_dict[illness]
                common_illness = illness
        return common_illness


    def paths_to_illness(self, illness):
        """
        This function receives a name of a illness, and with the
        root of the self-saved decision tree, it returns all paths to leaves
        with the name of the illness (as a True \ False list)
        """
        return self.paths_to_illness_helper([], [], self.__root, illness)


    def paths_to_illness_helper(self, paths_list, path, child, illness):
        """
        Recursive function that reaches all the leaves in the tree of the
        received root. If the illness received is saved in the leaf,
        the function will save the path to the leaf. The function returns
        a list of all the above paths
        """
        if not child.is_leaf(): #We got to the leaf
            if child.get_data() == illness:
                paths_list.append(path)
            return
        else:
            """
            From each symptom we proceed to the possibility
            that it is True and that is False
            """
            positive_path = copy.deepcopy(path)
            positive_path.append(True)
            self.paths_to_illness_helper(paths_list, positive_path,
                                         child.positive_child, illness)
            negative_path = copy.deepcopy(path)
            negative_path.append(False)
            self.paths_to_illness_helper(paths_list, negative_path,
                                         child.negative_child, illness)
            return paths_list


def build_tree(records, symptoms):
    """
    This function receives a list of records and a list of symptoms.
    The function will construct a tree, so that each path from the root
    to each of the leaves will be asked for all the symptoms in the symptom
    list. In the tree, there are all possible paths for True \ False answers
    to each of the symptoms. For each path, the function will check with
    the appropriate records for this path, which illness is the most common,
    and the same illness will define in the leaf at the end of the path.
    """
    root_tree = Node(symptoms[0], build_skeleton_tree(symptoms, 1),
                     build_skeleton_tree(symptoms, 1))
    """
    Sets the root of the tree by a recursive function that defines each
    node in the tree
    """
    bool_lists = bool_list(root_tree)
    # Creates all paths in the tree expressed using True \ False
    for bool_lst in bool_lists: #For each path in the tree:
        illness = find_illness(bool_lst, records, symptoms, root_tree)
        # A function that checks which illness is appropriate for the path
        illness_node = find_node(root_tree, bool_lst, 0)
        # A function that finds the node at the end of the path
        illness_node.set_data(illness)
        #Registration of the illness in the node
    return root_tree


def build_skeleton_tree(symptoms, stage):
    """
    Recursive function that builds a tree with all possible paths for
    True \ False answers to each of the symptoms. The function receives
    at each stage the stage at which it is located and the list of symptoms
    """
    if stage == len(symptoms): #We got to the leaf
        return Node("illness")
    child = Node(symptoms[stage], build_skeleton_tree(symptoms, stage + 1),
                 build_skeleton_tree(symptoms, stage + 1))
    return child


def bool_list(root_tree):
    """
    At this stage, all the leaves in the tree are marked "illness".
    The function will use the paths_to_illness function with the word
    "illness", which returns all the paths to the illness it receives,
    and thus our function returns all the paths in the tree
    """
    diagnoser = Diagnoser(root_tree)
    return diagnoser.paths_to_illness("illness")


def find_illness(bool_lst, records, symptoms, root_tree):
    """
    This function receives a boolean list that represents a path, a list of
    records, a list of symptoms and a tree root. The function will check
    which records correspond to the path (if for a particular symptom,
    the path is written False but the symptom is in the record, or True, but
    it is not in the record, the record is not appropriate). The illness in
    the appropriate records, the function will enter the dictionary as keys,
    so the value of each key is the number of times the illness has been
    adapted
    """
    illness_dict = {}
    diagnoser = Diagnoser(root_tree)
    for record in records:
        for i, symptom in enumerate(symptoms):
            if (symptom in record.symptoms and bool_lst[
                i - 1] == False) or (
                    symptom not in record.symptoms and bool_lst == True):
                """
                If one of the conditions is not met, the record does not match
                """
                break
        illness_dict = diagnoser.add_illness_to_dict(illness_dict,
                                                     record.get_illness())
        # Adds the appropriate records to the dictionary
    return diagnoser.most_common_illness_from_dict(illness_dict)


def find_node(child, bool_lst, i):
    """
    Recursive function that receives a node, a boolean list, and
    a stage in the path, and moves towards the node at the end of the path
    according to the True \ False at each stage
    """
    if i == len(bool_lst): #We have reached the requested node
        return child
    if bool_lst[i]:
        return find_node(child.positive_child, bool_lst, i + 1)
    else:
        return find_node(child.negative_child, bool_lst, i + 1)


def optimal_tree(records, symptoms, depth):
    """
    This function receives a list of records, a list of symptoms and a number
    depth- smaller than the size of the list of symptoms. The function
    returns a list of depth symptoms from the symptom list. The symptoms in
    this list will have a smaller error percentage in the calculate_error_rate
    function than any other combination of symptoms of size depth from the
    symptom list
    """
    smallest = MAX_ERROR_RATE
    root_tree = ""
    for symptoms_combination in list(itertools.combinations(symptoms, depth)):
        diagnoser = Diagnoser(build_tree(records,symptoms_combination))
        if diagnoser.calculate_error_rate(records) < smallest:
            smallest = diagnoser.calculate_error_rate(records)
            root_tree = build_tree(records,symptoms_combination)
    return root_tree





if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)


    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ",
              diagnosis)


# Add more tests for sections 2-7 here.
