#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print(f"Area: {my_square.area()} - Perimeter: {my_square.perimeter()}")
print(my_square)
