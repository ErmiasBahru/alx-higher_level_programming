#!/usr/bin/python3
"""Contain a single funtion"""
import json


def load_from_json_file(filename):
    """Return deserialized data from file"""
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    return data
