#!/usr/bin/python3
"""Class defination of student"""


class Student:
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes instance data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Retrieves the dictionary representationof  student
        """
        return self.__dict__
