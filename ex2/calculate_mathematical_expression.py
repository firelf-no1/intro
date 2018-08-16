##############################################################
# FILE : calculate_mathematical_expression.py
# WRITER : itai shopen , firelf , 021982038
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A simple program that gets an input of two numbers and an
# arithmetic sign and output an answer
#############################################################


def calculate_mathematical_expression(num1, num2, action1):
    # this function will take two input numbers and a string and give back an
    # answer
    x = float(num1)
    y = float(num2)
    if action1 == '-':
        # for Subtraction
        return y - x
    elif action1 == "/":
        # for Divide
        if y != 0:
            return x / y
        else:
            return None
    elif action1 == '+':
        # for addition
        return x + y
    elif action1 == '*':
        # for multiplication
        return x * y
    else:
        return None


def calculate_from_string(string1):
    # this function will take an input math problem and give back an answer
    num1, action1, num2 = string1.split()
    return calculate_mathematical_expression(float(num1), float(num2), action1)

print(calculate_from_string('9 / 5'))