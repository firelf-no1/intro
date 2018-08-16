##############################################################
# FILE : math_print.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex1 2017-2018
# DESCRIPTION: A simple program that prints solution to math eq
#############################################################
import math

def golden_ratio():
    # These next lines calculate the golden ratio
    print((1 + 5 ** 0.5) / 2)
    return

def six_square():
    # These next lines calculate 6 in the power of 2
    print(math.pow(6, 2))
    return

def hypotenuse():
    # These next lines calculate the hypotenuse of a triangle
    print(math.hypot(5, 12))
    return

def pi():
    # These next lines calculate the value of pi
    print(math.pi)
    return

def e():
     # These next lines calculate the value of e
     print(math.e)
     return
 

def squares_area():
     # These next lines calculate the surface of squares from 1 to 10
    for x in range(1,11):
         print(int(math.pow(x, 2)), end = " ")
     #print(int(1**2), int(2**2), int(3**2), int(4**2), int(5**2), int(6**2), int(7**2), int(8**2), int(9**2), int(10**2))
    print()
    return

golden_ratio()

six_square()

hypotenuse()

pi()

e()

squares_area()