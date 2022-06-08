#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, j in a_dictionary.items():
        if j == value:
            del a_dictionary[i]
            return complex_delete(a_dictionary, value)
    return a_dictionary
