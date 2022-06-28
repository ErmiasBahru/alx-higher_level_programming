#!/usr/bin/python3

"""
    Define a function that prints a text with 2 new line 
    after each of these characters: . , ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be string")

    start = 0
    delimeters = [".", ",", "?", ":"]

    for txt in text:
        if txt.isspace() and start == 0:
            continue
        elif txt in delimeters:
            print("{}\n\n".format(txt), end="")
            start = 0
            continue
        else:
            print("{}".format(txt), end="")
            start = start + 1
