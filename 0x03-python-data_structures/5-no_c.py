#!/usr/bin/python3
def no_c(my_string):
    new_value = list(my_string)
    for i in my_string:
        if i == 'c':
            new_value.remove('c')
        if i == 'C':
            new_value.remove('C')
        return ''.join(new_value)
