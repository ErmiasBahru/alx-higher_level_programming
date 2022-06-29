======================
How to use 101-lazy_matrix_mul.py
======================

Using ``lazy_matrix_mul``
-------------------

Importing the function from the module:
	>>> lazy_matrix_mul = __import__("101-lazy_matrix_mul").lazy_matrix_mul

Checking for module docstring:
	 >>> m = __import__("101-lazy_matrix_mul").__doc__
	 >>> len(m) > 1
	 True

Checking for function docstring:
	 >>> f = __import__("101-lazy_matrix_mul").lazy_matrix_mul.__doc__
         >>> len(f) > 1
         True

Checking for no args:
	 >>> lazy_matrix_mul()
	 Traceback (most recent call last):
	 ...
	 TypeError: lazy_matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

Checking for one too few args:
	 >>> lazy_matrix_mul([[1, 2], [3, 4]])
	 Traceback (most recent call last):
	 ...
	 TypeError: lazy_matrix_mul() missing 1 required positional argument: 'm_b'

Checking for too many args:
	 >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]])
	 Traceback (most recent call last):
	 ...
	 TypeError: lazy_matrix_mul() takes 2 positional arguments but 3 were given

Checking for normal use with ints and floats:
	 >>> print(lazy_matrix_mul([[1, 2], [3, 4]], [[1.5, 2.5, 3.5], [4.5, 6.5, 7.5]])) # doctest: +NORMALIZE_WHITESPACE
	 [[10.5   15.5   18.5]
	  [22.5   33.5   40.5]]

Checking for passing non-list as m_a:
	 >>> lazy_matrix_mul(None, [[1, 2], [3, 4]])
	 Traceback (most recent call last):
	 ...
	 TypeError: Object arrays are not currently supported

Checking for passing non-list to m_b:
	 >>> lazy_matrix_mul([[1, 2], [3, 4]], None)
	 Traceback (most recent call last):
	 ...
	 TypeError: Object arrays are not currently supported

Checking for passing empty m_a:
	 >>> lazy_matrix_mul([], [[1, 2], [3, 4]])
	 Traceback (most recent call last):
	 ...
	 ValueError: shapes (0,) and (2,2) not aligned: 0 (dim 0) != 2 (dim 0)

Checking for passing m_a with empty rows:
	 >>> lazy_matrix_mul([[], []], [[1, 2], [3, 4]])
	 Traceback (most recent call last):
	 ...
	 ValueError: shapes (2,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)

Checking for passing empty m_b:
	 >>> lazy_matrix_mul([[1, 2], [3, 4]], [])
	 Traceback (most recent call last):
	 ...
	 ValueError: shapes (2,2) and (0,) not aligned: 2 (dim 1) != 0 (dim 0)

Checking for passing m_b with empty rows:
	 >>> print(lazy_matrix_mul([[1, 2], [3, 4]], [[], []]))
	 []

Checking for uneven m_a:
	 >>> lazy_matrix_mul([[1, 2], [3, 4, 5]], [[1, 2], [3, 4]])
	 Traceback (most recent call last):
	 ...
	 ValueError: setting an array element with a sequence.

Checking for uneven m_b:
	 >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4, 5]])
	 Traceback (most recent call last):
	 ...
	 ValueError: setting an array element with a sequence.

Checking for non-number in list in m_a:
	 >>> lazy_matrix_mul([[1, "Hello"], [3, 4]], [[1, 2], [3, 4]])
	 Traceback (most recent call last):
	 ...
	 TypeError: invalid data type for einsum

Checking for non-number in list in m_b:
	 >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, "Hello"], [3, 4]])
	 Traceback (most recent call last):
	 ...
	 TypeError: invalid data type for einsum

Checking for mismatching matrices:
	 >>> lazy_matrix_mul([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4,]])
	 Traceback (most recent call last):
	 ...
	 ValueError: shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)
