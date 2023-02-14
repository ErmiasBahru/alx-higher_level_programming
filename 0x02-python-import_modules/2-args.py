#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('0 arguments.')
        exit()
    arg_num = len(sys.argv) - 1
    if len(sys.argv) == 2:
        print(f'{arg_num} argument:')
    else:
        print(f'{arg_num} arguments:')

    count = 0
    for i in sys.argv:
        count = count + 1
        if count == 1:
            continue
        print(f'{count - 1}: {i}')
