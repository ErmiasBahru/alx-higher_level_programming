#!/usr/bin/python3
"""Contain a single function"""
import json


def from_json_string(my_str):
    """Change string to json obj"""
    deserialized_json = json.loads(my_str)
    return deserialized_json
