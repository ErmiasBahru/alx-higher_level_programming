"""Contains unittest cases for `Square` class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests all methods and attributes of the `Square`
    class
    """
    def test_size(self):
        """Test creating `Square` with integer size"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_with_zero(self):
        """Test size with zero"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
            self.assertEqual(e, "width must be > 0")

    def test_size_with_negative(self):
        """Test size with negative number"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(-3)
            self.assertEqual(e, "width must be > 0")

    def test_size_string(self):
        """Test size with string"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("5k")
            self.assertEqual(e, "width must be an integer")

    def test_size_list(self):
        """Test size with list"""
        with self.assertRaises(TypeError) as e:
            s1 = Square([3, 5, 2, 4])
            self.assertEqual(e, "width must be an integer")

    def test_size_dict(self):
        """Test size with dictionary"""
        with self.assertRaises(TypeError) as e:
            s1 = Square({"n": 2, "b": 4})
            self.assertEqual(e, "width must be an integer")

    def test_size_tuple(self):
        """Test size with tuple"""
        with self.assertRaises(TypeError) as e:
            s1 = Square((3, 5, 2, 4))
            self.assertEqual(e, "width must be an integer")

    def test_size_float(self):
        """Test size with float"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(6.96)
            self.assertEqual(e, "width must be an integer")

    def test_size_nan(self):
        """Test size with not a number(nan)"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(float('nan'))
            self.assertEqual(e, "width must be an integer")

    def test_size_inf(self):
        """Test size with Infinity(inf)"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(float('inf'))
            self.assertEqual(e, "width must be an integer")

    def test_printing_square(self):
        """Test string output of `Square`"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

    def test_size_with_no_argument(self):
        """Test without argument supplied"""
        with self.assertRaises(TypeError) as e:
            s1 = Square()
            self.assertEqual(e, "__init__() missing 1 required \
                             positional argument: 'size'")

    def test_size_private(self):
        """Tests if size is an attribute of Square"""
        self.assertFalse(hasattr(Square, "_Square__size"))

    def test_area(self):
        """Testing area of `Square`"""
        Base._Base__nb_objects = 0
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)

    def test_with_id(self):
        """Test square string representation with id argument"""
        Base._Base__nb_objects = 0
        s1 = Square(6)
        s2 = Square(1)
        s3 = Square(3, 1, 3, 83)
        self.assertEqual(s3.__str__(), "[Square] (83) 1/3 - 3")

    def test_x_with_negative(self):
        """Test x with a negative integer"""
        with self.assertRaises(ValueError) as e:
            s3 = Square(3, -5, 3, 83)
            self.assertEqual(e, "x must be >= 0")

    def test_x_with_string(self):
        """Test x with a string"""
        with self.assertRaises(TypeError) as e:
            s3 = Square(3, "8", 3, 83)
            self.assertEqual(e, "x must be an integer")

    def test_y_with_negative(self):
        """Test y with a negative integer"""
        with self.assertRaises(ValueError) as e:
            s3 = Square(3, 5, -3, 83)
            self.assertEqual(e, "y must be >= 0")

    def test_y_with_string(self):
        """Test y with a string"""
        with self.assertRaises(TypeError) as e:
            s3 = Square(3, 8, "3", 83)
            self.assertEqual(e, "y must be an integer")

    def test_updating_id(self):
        """Testing for updating id"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")

    def test_updating_size(self):
        """Testing for updating size"""
        s1 = Square(5)
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")

    def test_updating_x(self):
        """Testing for updating x"""
        s1 = Square(5)
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

    def test_updating_y(self):
        """Testing for updating y"""
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_kwarg_update_1(self):
        """Testing updating x with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/0 - 5")

    def test_kwarg_update_2(self):
        """Testing updating size and x with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/1 - 7")

    def test_kwarg_update_3(self):
        """Testing updating id, y and size with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/1 - 7")

    def test_kwarg_update_4(self):
        """Testing updating all with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(size=7, id=89, y=1, x=4)
        self.assertEqual(s1.__str__(), "[Square] (89) 4/1 - 7")

    def test_update_without_arg(self):
        """Testing updating square without any argument passed"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update()
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

    def test_to_dictionary(self):
        """Testing `Square` to dictionary output"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(type(s1_dictionary), dict)
        self.assertDictEqual(s1_dictionary, {'id': 1, 'size': 10,
                                             'x': 2, 'y': 1})

    def test_save_to_file_empty_list(self):
        """Test saving to file with an empty list"""
        Base._Base__nb_objects = 0
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])
