#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print('{:d}{:d}'.format(i, j), end='')
            if i < 8:
                print(', ', end='')
print()
