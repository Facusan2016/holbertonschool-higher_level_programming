#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle

"""
    In this module we are testing the functions
    related to the base.py file using
    unittest.
"""


class TestRectangleClass(unittest.TestCase):

    def testBaseInheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def testRectangleIdFromBase(self):
        rec1 = Rectangle(4, 5, 1, 2, 66)
        self.assertEqual(rec1.id, 66)

    # Test Setters and getters.

    def testWidthAttr(self):
        rec1 = Rectangle(4, 5, 1, 2, 66)
        self.assertEqual(rec1.width, 4)
        rec1.width = 6
        self.assertEqual(rec1.width, 6)

    def testHeightAttr(self):
        rec1 = Rectangle(4, 5, 1, 2, 66)
        self.assertEqual(rec1.height, 5)
        rec1.height = 7
        self.assertEqual(rec1.height, 7)

    def testXAttr(self):
        rec1 = Rectangle(4, 5, 1, 2, 66)
        self.assertEqual(rec1.x, 1)
        rec1.x = 8
        self.assertEqual(rec1.x, 8)

    def testYAttr(self):
        rec1 = Rectangle(4, 5, 1, 2, 66)
        self.assertEqual(rec1.y, 2)
        rec1.y = 9
        self.assertEqual(rec1.y, 9)

    # TypeError Tests Width.

    def testWidthTypeErrorRaiseString(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle("Holberton", 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    def testWidthTypeErrorRaiseFloat(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(1.3, 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    def testWidthTypeErrorRaiseSet(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle({"Holberton", "School"}, 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    def testWidthTypeErrorRaiseList(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(["Holberton", "School"], 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    def testWidthTypeErrorRaiseBoolean(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(True, 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    def testWidthTypeErrorRaiseNone(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(None, 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    def testWidthTypeErrorRaiseNaN(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(float('NaN'), 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    def testWidthTypeErrorRaiseInf(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(float('Inf'), 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be an integer")

    # TypeError Tests Height.

    def testHeightTypeErrorRaiseString(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, "Holberton", 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    def testHeightTypeErrorRaiseFloat(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 1.3, 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    def testHeightTypeErrorRaiseSet(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, {"Holberton", "School"}, 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    def testHeightTypeErrorRaiseList(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, ["Holberton", "School"], 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    def testHeightTypeErrorRaiseBoolean(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, True, 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    def testHeightTypeErrorRaiseNone(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, None, 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    def testHeightTypeErrorRaiseNaN(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, float('NaN'), 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    def testHeightTypeErrorRaiseInf(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, float('Inf'), 3, 4)
            self.assertEqual(str(exc.exception), "height must be an integer")

    # TypeError Tests X.

    def testXTypeErrorRaiseString(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, "Holberton", 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    def testXTypeErrorRaiseFloat(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 1.3, 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    def testXTypeErrorRaiseSet(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, {"Holberton", "School"}, 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    def testXTypeErrorRaiseList(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, ["Holberton", "School"], 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    def testXTypeErrorRaiseBoolean(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, True, 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    def testXTypeErrorRaiseNone(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, None, 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    def testXTypeErrorRaiseNaN(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, float('NaN'), 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    def testXTypeErrorRaiseInf(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, float('Inf'), 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    # TypeError Tests Y.

    def testYTypeErrorRaiseString(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, "Holberton")
            self.assertEqual(str(exc.exception), "y must be an integer")

    def testYTypeErrorRaiseFloat(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, 1.3)
            self.assertEqual(str(exc.exception), "y must be an integer")

    def testYTypeErrorRaiseSet(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, {"Holberton", "School"})
            self.assertEqual(str(exc.exception), "y must be an integer")

    def testYTypeErrorRaiseList(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, ["Holberton", "School"])
            self.assertEqual(str(exc.exception), "y must be an integer")

    def testYTypeErrorRaiseBoolean(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, True)
            self.assertEqual(str(exc.exception), "y must be an integer")

    def testYTypeErrorRaiseNone(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, None)
            self.assertEqual(str(exc.exception), "y must be an integer")

    def testYTypeErrorRaiseNaN(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, float('NaN'))
            self.assertEqual(str(exc.exception), "y must be an integer")

    def testYTypeErrorRaiseInf(self):
        with self.assertRaises(TypeError) as exc:
            rec2 = Rectangle(2, 2, 4, float('Inf'))
            self.assertEqual(str(exc.exception), "y must be an integer")

    # ValueError Tests.

    def testWidthValueErrorRaiseZero(self):
        with self.assertRaises(ValueError) as exc:
            rec2 = Rectangle(0, 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be > 0")

    def testHeightValueErrorRaiseZero(self):
        with self.assertRaises(ValueError) as exc:
            rec2 = Rectangle(1, 0, 3, 4)
            self.assertEqual(str(exc.exception), "height must be > 0")

    def testWidthValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            rec2 = Rectangle(-5, 2, 3, 4)
            self.assertEqual(str(exc.exception), "width must be > 0")

    def testHeightValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            rec2 = Rectangle(1, -5, 3, 4)
            self.assertEqual(str(exc.exception), "height must be > 0")

    def testXValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            rec2 = Rectangle(1, 2, -5, 4)
            self.assertEquals(str(exc.exception), "x must be >= 0")

    def testYValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            rec2 = Rectangle(1, 2, 3, -5)
            self.assertEqual(str(exc.exception), "y must be >= 0")

    # Testing Area

    def testArea(self):
        rec3 = Rectangle(2, 2, 3, 4)
        self.assertEqual(rec3.area(), 4)

    # Overriding str default method.

    def testStr(self):
        rec5 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(rec5.__str__(), "[Rectangle] (6) 4/5 - 2/3")

    # Display 1

    def testPrintRectangle(self):
        rec6 = Rectangle(3, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rec6.display()
            self.assertEqual(fake_out.getvalue(), "\n ###\n ###\n")

    # Update 0

    def testRectangleUpdating(self):
        rec7 = Rectangle(2, 2, 1, 1, 20)
        rec7.update(34, 4, 4, 2, 2)
        self.assertEqual(rec7.__str__(), "[Rectangle] (34) 2/2 - 4/4")

    # Update 1

    def testRectangleUpdatingFromDict(self):
        rec8 = Rectangle(2, 2, 1, 1, 30)
        rec8.update(x=1, height=2, y=3, width=4, id=245)
        self.assertEqual(rec8.__str__(), "[Rectangle] (245) 1/3 - 4/2")
