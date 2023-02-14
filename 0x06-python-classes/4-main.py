#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print(f"Area: {my_square.area()} for size: {my_square.size}")

my_square.size = 3
print(f"Area: {my_square.area()} for size: {my_square.size}")

try:
    my_square.size = "5 feet"
    print(f"Area: {my_square.area()} for size: {my_square.size}")
except Exception as e:
    print(e)
