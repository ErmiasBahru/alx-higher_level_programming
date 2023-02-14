#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print(f"{a} comes from {int.__name__}")
if is_kind_of_class(a, float):
    print(f"{a} comes from {float.__name__}")
if is_kind_of_class(a, object):
    print(f"{a} comes from {object.__name__}")
