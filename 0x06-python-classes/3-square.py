#!/usr/bin/python3
"""Represent a square class"""


class Square:
    """Derives a square """
    def __init__(self, size=0):
        """Initializes the data
        Args:
            size (int): size of the square
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Raises:
            TypeError: when `size` isn't an integer
            ValueError: `size` is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square
        Returns: the area of the square
        """
        return (self.__size ** 2)
