#!/usr/bin/python3
"""Contains a `BaseGeometry` class"""


class BaseGeometry():
    """An empty BaseGeometry class"""

    def area(self):
        """Calculates the area of the geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the `value`"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
