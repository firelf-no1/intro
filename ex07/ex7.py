##############################################################
# FILE : ex7.py
# WRITER : itai shopen , firelf , 021982038
# EXERCISE : intro2cs ex7 2017-2018
# DESCRIPTION: linear and non linear Recursion
#############################################################


def print_to_n(n):
    """a program that print's all the positive numbers up to n from small to
     large"""
    if n > 1:
        print_to_n(n-1)
        print(n)
    elif n == 1:
        print(n)


def print_reversed(n):
    """a program that print's all the positive numbers up to n from large to
    small"""
    if n > 1:
        x = n
        print(x)
        print_reversed(n-1)
    elif n == 1:
        x = n
        print(x)


def has_divisor_smaller_then(n, i):
    """a function that's check if a number has any divider smaller then the
     input"""
    x = int(n ** 0.5)
    f = i
    if f <= x:
        if n%f == 0:
            return False
        if n%(f+2) == 0:
            return False
        f += 1
        if has_divisor_smaller_then(n, f) == False:
            return False
    else:
        return True


def is_prime(n):
    """a function to check if n is prime"""
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%3 == 0:
        return False
    f = 5
    if has_divisor_smaller_then(n, f) == False:
        return False
    else:
        return True


def divisors(n):
    """a function that calculate all the dividers of a number"""
    div_list = []
    if n < 0:
        x = -1 *n
        i = 1
        divisors_loop(x, i, div_list)
    if n >= 0:
        i = 1
        divisors_loop(n, i, div_list)
    return div_list


def divisors_loop(n, i, div_list):
    """a function that makes a loop for the function divisors"""
    if i <= n:
        if n % i == 0:
            div_list.append(i)
        divisors_loop(n, i+1, div_list)
    return div_list


def exp_n_x(n, x):
    """a function that calculate the mathematical term exp_n(x)‬‬"""
    exp_list = []
    i = 0
    k = 1
    exp_loop(n, x, i, k, exp_list)
    y = sum(exp_list)
    return y


def exp_loop(n, x, i, k, exp_list):
    """a function that makes a loop for the function exp_n_x"""
    if i <= n:
        exp_list.append((x**i)/k)
        exp_loop(n, x, i+1, k*(i+1), exp_list)
    return exp_list


def play_hanoi(hanoi, n, src, dest, temp):
    """a function to solve the tower of hanoi"""
    if n > 0:
        # move a tower the size of n - 1 to temp:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        # moves the disk from the source to the target poll
        hanoi.move(src, dest)
        # moves a tower the size of n-1 from temp to dest
        play_hanoi(hanoi, n - 1, temp, dest, src)


def print_binary_sequences(n):
    """finds binary sequences in n length"""
    if n < 0:
        return None
    if n == 0:
        t = ""
        print(t)
    if n > 0:
        for i in range(2**n):
            x = bin(i)[2:]
            y = "0" * (n-len(x)) + x
            print(y)


def sequences_loop(char_list, n):
    """a loop to find the sequences in a char list"""
    base = len(char_list)
    for i in range(base ** n):
        yield "".join(char_list[i // base ** (n - d - 1) % base]
                      for d in range(n))


def duplicate_checker(ans_list):
    """checks if there are duplicate in the input list"""
    seen = []
    for i in range(len(ans_list)):
        if ans_list[i] not in seen:
            seen.append(ans_list[i])
    return seen


def print_sequences(char_list, n):
    """Create all permutations of a string with repeating characters"""
    if n < 0:
        return None
    if n >= 0:
        for p in sequences_loop(char_list, n):
            print(p)


def print_no_repetition_sequences(char_list, n):
    """Create all permutations of a string with non-repeating characters"""
    ans_list = []
    if n >= 0:
        if n <= len(char_list):
            for p in sequences_loop(char_list, n):
                ans_list.append(p)
            final_list = duplicate_checker(ans_list)
            all_done = []
            for i in range(len(final_list)):
                a_list = []
                for j in range(n):
                    a_list.append(final_list[i][j])
                all_done.append(a_list)
            for i in range(len(all_done)):
                seen = []
                for j in range(len(all_done[i])):
                    if all_done[i][j] not in seen:
                        seen.append((all_done[i][j]))
                if len(seen) == len(all_done[i]):
                    x = ''.join(all_done[i])
                    print(x)
        else:
            return None
    else:
        return None


def no_repetition_sequences_list(char_list, n):
    """Create all permutations of a string with non-repeating characters and
     gives a string output"""
    if len(char_list) >= n:
        ans_list = []
        for p in sequences_loop(char_list, n):
            ans_list.append(p)
        final_list = duplicate_checker(ans_list)
        all_done = []
        for i in range(len(final_list)):
            a_list = []
            for j in range(n):
                a_list.append(final_list[i][j])
            all_done.append(a_list)
        new_list = []
        for i in range(len(all_done)):
            seen = []
            for j in range(len(all_done[i])):
                if all_done[i][j] not in seen:
                    seen.append((all_done[i][j]))
            if len(seen) == len(all_done[i]):
                new_list.append(''.join(all_done[i]))
        return new_list

    else:
        return None



