##############################################################
# FILE : shapes.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A simple program that gets an input of a shape and gives
# back the area size
#############################################################
import math


def shape_area():
    # a simple function that calculate the given shape size
    shape = input('choose shape (1=circle, 2=rectangle, 3=trapezoid): ')
    # wait for user
    x = int(shape)
    if x == 1:
        # calculate the area of a circle
        r = float(input(''))
        # wait for user input
        s1 = (r**2)*math.pi
        return s1
    elif x == 2:
        # calculate the area of a rectangle
        a = float(input (''))
        # wait for user input
        b = float(input (''))
        # wait for user input
        s2 = (a*b)
        return s2
    elif x == 3:
        # calculate the area of a trapezoid
        a = float(input (''))
        # wait for user input
        b = float(input (''))
        # wait for user input
        h = float(input (''))
        # wait for user input
        s3 = (((a+b)/2)*h)
        return s3
    else:
        return 'end'
