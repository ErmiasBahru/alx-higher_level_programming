#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_list.sort()
        return((my_list[-1]))
