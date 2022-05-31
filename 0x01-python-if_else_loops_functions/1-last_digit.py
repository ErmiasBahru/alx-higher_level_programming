#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
print('Last digit of {} is {} and is'.format(number, last_digit), end='')
if last_digit > 5:
    print('greater than 5')
elif last_digit == 0:
    print('0')
else:
    print('less than 6 and not 0')
