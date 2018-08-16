##############################################################
# FILE : largest_and_smallest.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A simple program that gets an input of three numbers and gives
# back the largest and smallest
#############################################################


def largest_and_smallest(x, y, z):
    #  this function finds the largest and smallest number out of the
    #  three inputs
    num1 = int(x)
    num2 = int(y)
    num3 = int(z)
    if num1 >= num2:
        if num1 >= num3:
            if num3 >= num2:
                return num1, num2
            else:
                return num1, num3
        else:
            return num3, num2
    else:
        if num2 >= num3:
            if num3 >= num1:
                return num2, num1
            else:
                return num2, num3
        else:
            return num3, num1


