#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")

print(my_rectangle)
print(repr(my_rectangle))

print("--")
