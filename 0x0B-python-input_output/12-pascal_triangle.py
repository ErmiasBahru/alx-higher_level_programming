#!/usr/bin/python3
"""Contains a single function that draws a pascal triangle"""


def pascal_triangle(n):
    """creates a list of pascal triangle"""
    my_list = [[0 for j in range(i + 1)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                my_list[i][j] = 1
            elif j == i:
                my_list[i][j] = 1
            else:
                my_list[i][j] = my_list[i-1][j] + my_list[i-1][j-1]
    return my_list
