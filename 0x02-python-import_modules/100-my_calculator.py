#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    if operator == '*':
        print(f'{a} * {b} = {mul(a, b)}')
    elif operator == '+':
        print(f'{a} + {b} = {add(a, b)}')
    elif operator == '-':
        print(f'{a} - {b} = {sub(a, b)}')
    elif operator == '/':
        print(f'{a} / {b} = {div(a, b)}')
