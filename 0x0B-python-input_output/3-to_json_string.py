#!/usr/bin/python3
"""Contain a single function """
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    json_obj = json.dumps(my_obj)
    return json_obj
