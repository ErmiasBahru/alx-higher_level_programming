#!/usr/bin/python3
"""
    Contains a single function that prints out names
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "":
        raise ValueError("first_name is required")

    print("My name is {} {}".format(first_name, last_name))
