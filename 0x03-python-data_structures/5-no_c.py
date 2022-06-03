#!/usr/bin/python3
def no_c(my_string):
    new_value = []
    for i in my_string:
        if i != 'c' and i != 'C':
            new_value.append(i)
        return ''.join(new_value)
