#!/usr/bin/python3

class Base:
    """
        Defines the class `base`

        Attributes: 
            id (int): instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects