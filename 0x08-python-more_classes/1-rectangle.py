#!/usr/bin/python3
"""
    Module contains of a single class
"""


class Rectangle:
    """Defines a reactangle"""

    def __init__(self, width=0, height=0):
        """Initializing of instance data"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the value of `width`"""
        return self.__width

    @property
    def height(self):
        """Retrieves the value of `height`"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the value of atribute `width` to new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value of atribute `height` to new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
