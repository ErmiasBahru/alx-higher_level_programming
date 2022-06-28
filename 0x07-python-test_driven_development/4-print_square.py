#!/usr/bin/python3
"""
    Contains a single function that prints a square
"""


def print_square(size):
    """Prints a square with the character `#`"""

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size) if isinstance(size, float) else size
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
