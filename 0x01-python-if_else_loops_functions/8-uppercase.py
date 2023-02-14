#!/usr/bin/python3
def uppercase(str):
    case = 0
    for i in str:
        case = 32 if ord(i) >= ord('a') and ord(i) <= ord('z') else 0
        print('{:c}'.format(ord(i) - case), end='')
    print()
