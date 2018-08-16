##############################################################
# FILE : ex3.py
# WRITER : itai shopen , firelf , 021982038
# EXERCISE : intro2cs ex3 2017-2018
# DESCRIPTION: loops
#############################################################
# !/usr/bin/env python3


def create_list():
    # A program that gets an input from the user and creates a list of the
    #  input
    lst1 = list()
    while 1:
        string_from_user = input('')
        # wait for user
        if bool(string_from_user) != False:
            lst1.append(string_from_user)
        else:
            return lst1
    pass



def concat_list(str_list):
    # A program that gets a string from the user and returns a connected list
    concatenation = str()
    for string in str_list:
        concatenation += string
    return concatenation
    pass

def average(num_list):
    # A program that gets a string of numbers and returns their average
    num_sum = int()
    if len(num_list) == 0:
        return None
    else:
        for num in num_list:
            num_sum += num
        final_average = num_sum / len(num_list)
        return final_average
    pass


def cyclic(lst1, lst2):
    # A program that get 2 lists and checks if they are cyclic permutation of
    # eachother
    if len(lst1) != len(lst2):
        return False
    if lst1 == lst2:
        return True
    for i in range(1, len(lst2)):
        run_sum = 0
        for m in range(0, len(lst1)):
            if lst1[m] == lst2[(i+m)%len(lst2)]:
                run_sum += 1
        if run_sum == len(lst1):
            return True
    else:
        return False
    pass



def histogram(n, num_list):
    # A program that counts the number of time a number is in that list
    histo_list = list()
    for i in range(0, n):
        place_counter = 0
        for num in range(0, len(num_list)):
            if num_list[num] == i:
                place_counter += 1
        histo_list.append(place_counter)
    return histo_list
    pass

def prime_factors(n):
    # A program that gets a number and return the prime dividers
    i = 2
    prime_list = list()
    while i <= n:
        while n%i == 0:
            n = n / i
            prime_list.append(i)
        i = i + 1
    return prime_list
    pass


def cartesian(lst1, lst2):
    # A program that takes 2 lists and gives back a cartesian product
    tup_list = list()
    if len(lst1) == 0 or len(lst2) == 0:
        return []
    for i in range(0, len(lst1)):
        for m in range(0, len(lst2)):
            tup1 = lst1[i], lst2[m]
            tup_list.append(tuple(tup1))
    return tup_list
    pass


def pairs(n, num_list):
    # A program that check if there are pairs of numbers in a list that add up
    #  to a test number
    caples_list = list()
    for i in range(0, len(num_list)):
        for m in range((i+1), len(num_list)):
            if n == num_list[i] + num_list[m]:
                caples_list.append([num_list[i], num_list[m]])
    return caples_list
    pass


from datetime import datetime
n=    48947  *  77093 *  77101  * 77137
print('Start :', str(datetime.now()))
print(prime_factors( n ))
print('End :', str(datetime.now()))