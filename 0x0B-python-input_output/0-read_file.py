#!/usr/bin/python3
"""Contain a single function that read files"""


def read_file(filename=""):
    """Reads and prints content of file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
