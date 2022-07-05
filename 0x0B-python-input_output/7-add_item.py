#!/usr/bin/python3
"""Handles file input and saves to file"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


argv.pop(0)
try:
    deserialized = load_from_json_file("add_item.json")
    if deserialized is None:
        save_to_json_file(argv, "add_item.json")
    else:
        deserialized.extend(argv)
        save_to_json_file(deserialized, "add_item.json")
except FileNotFoundError:
    save_to_json_file(argv, "add_item.json")
