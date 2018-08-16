##############################################################
# FILE : quadratic_equation.py
# WRITER : itai shopen , firelf , 021982038
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A simple program that gets an input of quadratic equation and
#  gives back a solution
#############################################################


def quadratic_equation(x, y, z):
    # this function will find the roots of a quadratic equation
    a = float(x)
    b = float(y)
    c = float(z)
    root = b ** 2 - 4 * a * c
    if root >= 0:
        root1 = root**0.5
        x1 = (-b + root1) / (2 * a)
        x2 = (-b - root1) / (2 * a)
        if x1 == x2:
            return x1, None
        else:
            return x1, x2
    else:
        return None, None


def quadratic_equation_user_input():
    string = input('insert coefficients a, b, and c: ')
    # wait for user input
    x, y, z = string.split()
    x1, x2 = quadratic_equation(x, y, z)
    if x1 == x2:
        return 'The equation has no solutions'
    else:
        if x2 is not None:
            return 'The equation has two solution: ' + str(x1) + ' and '\
                   + str(x2)
        else:
            return 'The equation has one solution:' + str(x1)

