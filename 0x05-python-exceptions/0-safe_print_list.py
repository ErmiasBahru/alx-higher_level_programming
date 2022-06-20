#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        element = 0
        while element < x:
            print(my_list[element], end='')
            element = element + 1
        print()
    except:
        print()
    return element
