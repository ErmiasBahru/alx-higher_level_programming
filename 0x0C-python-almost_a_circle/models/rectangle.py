#!/usr/bin/python3
"""Contains class `Rectangle` defination"""
from .base import Base


class Rectangle(Base):
    """Derives the class that inherits form `Base` class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            width (int): width of the ractangle
            height (int): height of rectangle
            x (int): x axis of rectangle
            y (int): y axis of the rectangle
            id (int): id of the rectangle
        """
        self.validate_input(width=width, height=height, x=x, y=y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """Returns string representation of the instance"""
        string = "[{}] ({}) {}/{} - {}"
        if type(self) == Rectangle:
            return "{}/{}".format(string.format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width), self.__height)
        return string.format(self.__class__.__name__, self.id, self.__x,
                             self.__y, self.__width)

    @staticmethod
    def validate_input(**kwargs):
        """Validates the values before assigning them to
        instance attributes
        """
        for name, value in kwargs.items():
            if name == "x" or name == "y":
                if type(value) != int:
                    raise TypeError("{} must be an integer".format(name))
                elif value < 0:
                    raise ValueError("{} must be >= 0".format(name))
            else:
                if type(value) != int:
                    raise TypeError("{} must be an integer".format(name))
                elif value <= 0:
                    raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """Retrieves the value of `width`
        Returns:
            value of width
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the value of `height`
        Returns:
            value of height
        """
        return self.__height

    @property
    def x(self):
        """Retrieves the value of `x`
        Returns:
            value of x
        """
        return self.__x

    @property
    def y(self):
        """Retrieves the value of `y`
        Returns:
            value of y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """sets the value of `width`"""
        self.validate_input(width=value)
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value of `height`"""
        self.validate_input(height=value)
        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value of `x`"""
        self.validate_input(x=value)
        self.__x = value

    @y.setter
    def y(self, value):
        """sets the value of `y`"""
        self.validate_input(y=value)
        self.__y = value

    def area(self):
        """Calculates the area of `Rectangle` instance
        Returns:
            Calculated area of a Rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the
        character `#`
        """
        [print() for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for i in range(self.__x)]
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Updates the values of the class"""
        if args and len(args) > 0:
            keys = ["id", "width", "height", "x", "y"]
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
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
        return dictionary
