#!/usr/bin/python3
"""Contains a class `MyInt` that inherits from `int`"""


class MyInt(int):
    """Inherits from int base class"""
    def __init__(self, value):
        """Initialize value"""
        self.value = value

    def __ne__(self, x):
        """not equal to comparison"""
        if self.value is x:
            return True

    def __eq__(self, x):
        """equal to comparison"""
        return not self.__ne__(x)
