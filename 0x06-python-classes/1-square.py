#!/usr/bin/python3
"""a square class"""


class Square:
    """Derives a square """
    def __init__(self, size):
        """Initializes attributes
        Args:
            size (int): value to initialize `size`
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        """
        self.__size = size
