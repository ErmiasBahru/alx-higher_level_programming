#!/usr/bin/python3
"""Contains `Square` class defination"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Class inherits from `Rectangle` class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            size (int): size of rectangle
            x (int): x axis of rectangle
            y (int): y axis of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the value of `size`
        Returns:
            value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the dimensions of `Square`"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the class"""
        if args and len(args) > 0:
            keys = ["id", "size", "x", "y"]
            for i, v in enumerate(args):
                setattr(self, keys[i], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Retrieves all the attributes of class to dictionary
        Returns:
            dictionary containing it's attributes
        """
        dictionary = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
        return dictionary
