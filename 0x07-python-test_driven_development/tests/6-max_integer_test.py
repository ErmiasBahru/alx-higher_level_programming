#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_int(self):
        """Test valid integers."""
        self.assertEqual(max_integer([10, -20, 30, -40]), 30)
        self.assertEqual(max_integer([50]), 50)
        self.assertEqual(max_integer([0, -5, -10]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-2, -6, -8, -4]), -2)

    def test_type(self):
        """Test other compatible data types."""
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 3)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

if __name__ == '__main__':
    unittest.main()

