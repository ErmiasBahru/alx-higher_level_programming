#!/usr/bin/python3
"""Contains a single function"""


def inherits_from(obj, a_class):
    """
        Check if the object is instance of a class inherited
        from directly or indirectly
    """
    return ((issubclass(type(obj), a_class)) and type(obj) != a_class)
