"""Contains test cases of `Rectangle` class which extends the `Base` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the ractangle class"""
    def width_height_integers(self):
        """Tests for width and height as integers"""
        Base._Base.__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def with_all_arguments(self):
        """Test with all valid arguments"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_for_private_width(self):
        """Testing for width as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__width"))

    def test_for_private_height(self):
        """Test for height as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__height"))

    def test_for_private_x(self):
        """Test for x as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__x"))

    def test_for_private_y(self):
        """Test for y as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__y"))

    def width_setter_getter_with_int(self):
        """Test width setter and getter with integers"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        r3.width = 5
        self.assertEqual(r3.width, 5)

    def height_setter_getter_with_int(self):
        """Test height setter and getter with integers"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        r3.height = 5
        self.assertEqual(r3.height, 5)

    def width_setter_getter_with_other_type(self):
        """Test width setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r3.width = "5"

    def height_setter_getter_with_other_type(self):
        """Test height setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r3.height = "5"

    def width_with_string(self):
        """Test width with string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle("2", 2)

    def width_with_negative(self):
        """Test width with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(-2, 3)

    def width_with_zero(self):
        "Test width with zero"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 3)

    def height_with_string(self):
        """Test height setter and geter with other data type"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, "2")

    def height_with_negative(self):
        """Test height with seter and getter with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, -3)

    def height_with_zero(self):
        "Test setter and getter with zero"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 3)

    def test_with_no_argument(self):
        """Test with no argument supplied"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle()

    def x_with_string(self):
        """Test x with string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, "5", 4)

    def x_with_negative(self):
        """Test x with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 3, -5, 4)

    def y_with_string(self):
        """Test y with string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, 5, "4")

    def y_with_negative(self):
        """Test y with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 3, 5, -4)

    def width_with_tupple(self):
        """Test for width with tuple"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle((4, 6), 3, 5, 4)

    def width_with_dictionary(self):
        """Test for width with dictionary"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle({"name": "alex", "other_name": "steve"}, 3, 5, 4)

    def width_with_float(self):
        """Test for width with float"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(8.86, 3, 5, 4)

    def width_with_list(self):
        """Test for width with list"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle([5, 2, 6], 3, 5, 4)

    def width_with_nan(self):
        """Test for width with nan"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(float('nan'), 3, 5, 4)

    def width_with_inf(self):
        """Test for width with inf"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(float('inf'), 3, 5, 4)

    def height_with_tupple(self):
        """Test for height with tuple"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, (4, 6), 5, 4)

    def height_with_dictionary(self):
        """Test for height with dictionary"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, {"name": "alex", "other_name": "steve"}, 5, 4)

    def height_with_float(self):
        """Test for height with float"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(6, 3.642, 5, 4)

    def height_with_list(self):
        """Test for height with list"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, [5, 2, 6], 5, 4)

    def height_with_nan(self):
        """Test for height with nan"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, float('nan'), 5, 4)

    def height_with_inf(self):
        """Test for height with inf"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, float('inf'), 5, 4)

    def x_setter_getter_with_other_type(self):
        """Test x setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3, 4, 6)
        with self.assertRaises(TypeError):
            r3.x = "5"

    def y_setter_getter_with_other_type(self):
        """Test y setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3, 7, 8)
        with self.assertRaises(TypeError):
            r3.y = "5"

    def test_for_area(self):
        """Testing for area"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_for_str_with_id(self):
        """Test formatted output class to string with id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_for_str_without_id(self):
        """Test formatted output class to string without id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/1 - 4/6")

    def test_updating_id(self):
        """Testing for updating id"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_updating_width(self):
        """Testing for updating width"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_updating_height(self):
        """Testing for updating height"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_updating_x(self):
        """Testing for updating x"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

    def test_updating_y(self):
        """Testing for updating y"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_kwarg_update_1(self):
        """Testing  updating width and x with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/10")

    def test_kwarg_update_2(self):
        """Testing updating y, x, width, id with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwarg_update_3(self):
        """Testing updating x, height, y and width with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/3 - 4/2")

    def test_kwarg_update_4(self):
        """Testing updating height with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_to_dictionary(self):
        """Testing `Rectangle` to dictionary output"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)
        self.assertDictEqual(r1_dictionary, {'id': 1, 'width': 10,
                                             'height': 2, 'x': 1, 'y': 9})
