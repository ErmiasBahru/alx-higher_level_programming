#!/usr/bin/python3
""" Roman to Integer test file
"""

roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "VII"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "IX"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "LXXXVII"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "DCCVII"
print(f"{roman_number} = {roman_to_int(roman_number)}")
