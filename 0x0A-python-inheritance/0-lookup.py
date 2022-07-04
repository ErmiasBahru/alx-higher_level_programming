#!/usr/bin/python3

"""Module for a lookup function"""


def lookup(obj):
    """
        Return list of available object and methods
        in an object
    """
    return dir(obj)
