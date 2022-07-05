#!/usr/bin/python3
"""Contain a single funtion"""
import json


def save_to_json_file(my_obj, filename):
    """Save json content to file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
