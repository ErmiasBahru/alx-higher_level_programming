#!/usr/bin/python3
""" contains function that finds a peak in a list
    of unsorted integers.
"""


def find_peak(list_of_integers):
    """Function finds peak of list passed in"""
    if type(list_of_integers) != list:
        return
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
