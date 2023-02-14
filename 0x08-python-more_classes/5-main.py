#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print(f"[{e.__class__.__name__}] {e}")
