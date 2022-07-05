#!/usr/bin/python3
"""Contains a function that write to file"""


def write_file(filename="", text=""):
    """
        Writes the content `text` to a file specified
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
