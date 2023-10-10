#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

"""
    In this module we are testing the functions
    related to the square.py file using
    unittest.
"""


class TestSquareClass(unittest.TestCase):

    def testBaseInheritanceSquare(self):
        self.assertTrue(issubclass(Square, Base))

    def testRectangleInheritanceSquare(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def testSquareIdFromBase(self):
        sqr1 = Square(5, 1, 2, 66)
        self.assertEqual(sqr1.id, 66)

    def testBasicInitInheretedWidthMethod(self):
        sqr2 = Square(3, 2, 2)
        self.assertEqual(sqr2.width, 3)

    def testBasicInitInheretedHeightMethod(self):
        sqr2 = Square(3, 2, 2)
        self.assertEqual(sqr2.height, 3)

    def testBasicInitInheretedXMethod(self):
        sqr2 = Square(3, 1, 2)
        self.assertEqual(sqr2.x, 1)

    def testBasicInitInheretedYMethod(self):
        sqr2 = Square(3, 1, 2)
        self.assertEqual(sqr2.y, 2)

    def testSizeGetter(self):
        sqr2 = Square(3, 1, 2)
        self.assertEqual(sqr2.size, 3)

    def testSizeSetter(self):
        sqr2 = Square(3, 1, 2)
        sqr2.size = 5
        self.assertEqual(sqr2.size, 5)

    def testSizeSetterWidth(self):
        sqr2 = Square(3, 1, 2)
        sqr2.size = 5
        self.assertEqual(sqr2.width, 5)

    def testSizeSetterHeight(self):
        sqr2 = Square(3, 1, 2)
        sqr2.size = 5
        self.assertEqual(sqr2.height, 5)

    def testSizeSetterWrong(self):
        with self.assertRaises(TypeError) as exc:
            sqr2 = Square("Holberton", 1, 2)
            self.assertEqual(str(exc.exception), "width must be an integer")

    # TypeError Tests X.

    def testXTypeErrorRaiseString(self):
        with self.assertRaises(TypeError) as exc:
            sqr2 = Square(2, "Holberton", 4)
            self.assertEqual(str(exc.exception), "x must be an integer")

    # TypeError Tests Y.

    def testYTypeErrorRaiseString(self):
        with self.assertRaises(TypeError) as exc:
            sqr2 = Square(2, 4, "Holberton")
            self.assertEqual(str(exc.exception), "y must be an integer")

    # ValueError Tests.

    def testWidthValueErrorRaiseZero(self):
        with self.assertRaises(ValueError) as exc:
            sqr2 = Square(0, 3, 4)
            self.assertEqual(str(exc.exception), "width must be > 0")

    def testHeightValueErrorRaiseZero(self):
        with self.assertRaises(ValueError) as exc:
            sqr2 = Square(0, 3, 4)
            self.assertEqual(str(exc.exception), "height must be > 0")

    def testWidthValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            sqr = Square(-5, 3, 4)
            self.assertEqual(str(exc.exception), "width must be > 0")

    def testHeightValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            sqr2 = Square(-5, 3, 4)
            self.assertEqual(str(exc.exception), "height must be > 0")

    def testXValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            sqr2 = Square(1, -5, 4)
            self.assertEquals(str(exc.exception), "x must be >= 0")

    def testYValueErrorRaise(self):
        with self.assertRaises(ValueError) as exc:
            sqr2 = Square(2, 3, -5)
            self.assertEqual(str(exc.exception), "y must be >= 0")

    def testSquareUpdating(self):
        sqr3 = Square(2, 1, 1, 20)
        sqr3.update(34, 4, 2, 2)
        self.assertEqual(sqr3.__str__(), "[Square] (34) 2/2 - 4")

    def testSquareUpdatingFromDict(self):
        sqr3 = Square(3, 1, 1, 30)
        sqr3.update(size=7, id=89, y=1)
        self.assertEqual(sqr3.__str__(), "[Square] (89) 1/1 - 7")

    def testSquareToDictionary(self):
        s1 = Square(10, 2, 1, 1)
        res = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), res)
