#!/usr/bin/python3

"""
    Define a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str):
        raise TypeError("first_name must be string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name == "":
        raise ValueError("first_name is required")

    print("My name is {} {}".format(first_name, last_name))