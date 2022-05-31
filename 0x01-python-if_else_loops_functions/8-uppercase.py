#!/usr/bin/python3
def uppercase(str):
    case = 0
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            case = 32
        else:
            case = 0
        print('{:c}'.format(ord(i) - case), end='')
    print()
