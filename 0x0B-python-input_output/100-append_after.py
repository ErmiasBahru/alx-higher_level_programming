#!/usr/bin/python3
"""Contains function that handles appending"""


def append_after(filename="", search_string="", new_string=""):
    """
        Append a new string if certain string is encountered
        in the line
        Args:
            filename (str): name of file
            search_string (str): string to be searched
            new_string (str): string to be appended
    """
    lines = ""
    with open(filename, encoding="utf-8", mode="r") as f:
        readline = f.readline()
        while readline:
            lines += readline
            if search_string in readline:
                lines += new_string
            readline = f.readline()
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(lines)
