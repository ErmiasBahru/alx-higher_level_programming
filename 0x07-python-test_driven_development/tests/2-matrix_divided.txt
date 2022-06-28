================================
 How to Use 2-matrix_divided.py
================================

This module contains only a single function

``2-matrix_divided.py(matrix, div)``

Which divides all elements of a matrix and returns a new matrix

Numbers
=======

``2-matrix_divided.py`` returns a new resulting matrix based on division
with it's second argument

>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Matrix with equal sized rows with integers

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

>>> print(matrix)
[[1, 2, 3], [4, 5, 6]]

Matrix with equal sized rows with floats

>>> matrix = [[1, 2, 3.6], [4.7, 6.23, 6]]
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.2], [1.57, 2.08, 2.0]]

Case div is a float

>>> print(matrix_divided(matrix, 3.2))
[[0.31, 0.62, 1.12], [1.47, 1.95, 1.88]]


Exceptions
=========

while ``2-matrix_divided.py`` performs divisions to matrix it also limits
what user passes to it

Example passing a dictionary instead of matrix list

>>> matrix = ([1, 2, 3], [4, 5, 6])
>>> print(matrix_divided(matrix, 3))
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

Example passing a matrix with other data types instead of a list

>>> matrix = [(1, 2, 3), [4, 5, 6]]
>>> print(matrix_divided(matrix, 3))
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

Example matrix but with rows containing non float or int data types

>>> matrix = [[1, 2, "holberton"], [4, 5, 6]]
>>> print(matrix_divided(matrix, 3))
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

Example passing matrix with unequal row sizes

>>> matrix = [[1, 2, 3], [4, 5]]
>>> print(matrix_divided(matrix, 3))
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

Example when div argument passed isn't float or int

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> print(matrix_divided(matrix, "holberton"))
Traceback (most recent call last):
TypeError: div must be a number

Example when div is zero

>>> print(matrix_divided(matrix, 0))
Traceback (most recent call last):
ZeroDivisionError: division by zero

Case where either one arguments is missing

>>> print(matrix_divided(0))
Traceback (most recent call last):
TypeError: matrix_divided() missing 1 required positional argument: 'div'

Case where both arguments are missing

>>> print(matrix_divided())
Traceback (most recent call last):
TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
