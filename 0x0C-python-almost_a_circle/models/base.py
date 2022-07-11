#!/usr/bin/python3
"""Contains a class `Base`"""
import json


class Base:
    """
        Defines the class `Base`

        Attributes:
            id (int): instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes class and object data

            Args:
                id (int): integer passed on object creation
        """
        self.id = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionaries to their string
        representation i.e JSON
        """
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `list_objs`
        to a file
        """
        if list_objs is None:
            data = []
        else:
            data = [i.to_dictionary() for i in list_objs]
        string = cls.to_json_string(data)
        filename = "{}.json".format(cls.__name__)

        with open(filename, encoding="utf-8", mode="w") as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """Changes json string to a list
        Returns:
            list of dictionaries
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Adds a class method
        Returns:
            returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads data from file and uses it to get instances associated
        Returns:
            a list of instances:
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, encoding="utf-8") as f:
                string = f.read()
        except FileNotFoundError:
            return []

        json = cls.from_json_string(string)
        instances = [cls.create(**instance) for instance in json]
        return instances
