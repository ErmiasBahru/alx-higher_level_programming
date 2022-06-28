#!/usr/bin/python3
"""
    Contains a single function that handles text indenting
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each
        of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    begin = 0
    delimeters = [".", "?", ":"]
    for c in text:
        if c.isspace() and begin == 0:
            continue
        elif c in delimeters:
            print("{}\n\n".format(c), end="")
            begin = 0
            continue
        else:
            print("{}".format(c), end="")
            begin += 1
