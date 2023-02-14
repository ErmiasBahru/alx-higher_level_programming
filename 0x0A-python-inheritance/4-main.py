#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print(f"{a} inherited from class {int.__name__}")
if inherits_from(a, bool):
    print(f"{a} inherited from class {bool.__name__}")
if inherits_from(a, object):
    print(f"{a} inherited from class {object.__name__}")
