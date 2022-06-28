#!/usr/bin/python3

"""
    Define a function that prints a square with the character #
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    size = int(size) if isinstance(size, float) else size

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
