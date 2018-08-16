##############################################################
# FILE : hello_turtle.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex1 2017-2018
# DESCRIPTION: A simple program that prints a flower bed
#############################################################
import turtle


def drew_petal():
    # These next lines draw a petal
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    return


def drew_flower():
    # These next lines draw a flower
    turtle.left(45)
    drew_petal()
    turtle.left(90)
    drew_petal()
    turtle.left(90)
    drew_petal()
    turtle.left(90)
    drew_petal()
    turtle.left(135)
    turtle.forward(150)
    return


def drew_flower_advanced():
    # These next lines draw a flower and move the head
    drew_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()
    return


def drew_flower_bed():
    # These next lines draw a flower bed
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    drew_flower_advanced()
    drew_flower_advanced()
    drew_flower_advanced()
    return


drew_flower_bed()

turtle.done()
