#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print(f"{a} is an instance of the class {int.__name__}")
if is_same_class(a, float):
    print(f"{a} is an instance of the class {float.__name__}")
if is_same_class(a, object):
    print(f"{a} is an instance of the class {object.__name__}")
