#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    numarg = 0
    for num in argv[1:]:
        numarg = numarg + int(num)
    print(numarg)
