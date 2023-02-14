#!/usr/bin/python3
"""Contain a single function"""
import json


def from_json_string(my_str):
    """Change string to json obj"""
    return json.loads(my_str)
