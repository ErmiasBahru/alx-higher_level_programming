#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    if x == 0:
        print()
        return i
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
    except IndexError:
        print()
        return i
    return i + 1
