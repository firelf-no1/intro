##############################################################################
# FILE : temperature.py
# WRITER : itai shopen
# EXERCISE : intro2cs ex2 2017-2018
# DESCRIPTION: A simple program that gets an input of a test temperature and
#  the temperature from the last 3 days and gives back the answer is it summer
##############################################################################


def is_it_summer_yet(test_temp, temp_day1, temp_day2, temp_day3):
    # this function will determine if it's summer
    if temp_day1 > test_temp:
        if temp_day2 > test_temp:
            return True
        elif temp_day3 > test_temp:
            return True
        else:
            return False
    elif temp_day2 > test_temp:
        if temp_day3 > test_temp:
            return True
        else:
            return False
    else:
        return False
