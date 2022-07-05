#!/usr/bin/python3
"""Contain a function that appends to file"""


def append_write(filename="", text=""):
    """Handles content appendint to file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
