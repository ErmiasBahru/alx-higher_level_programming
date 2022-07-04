#!/usr/bin/python3
"""Module contains implementation of `Square` class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from class `Rectangle`"""
    def __init__(self, size):
        """Initializes the values"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Prints the description of the `Rectangle`"""
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
