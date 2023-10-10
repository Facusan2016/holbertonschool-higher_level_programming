#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle

"""
    In this module we are testing the functions
    related to the base.py file using
    unittest.
"""


class TestBaseClass(unittest.TestCase):

    def testId(self):
        id_obj = Base(45)
        self.assertEqual(id_obj.id, 45)

    def testPrivateNbObjectInc(self):
        noneObj = Base()
        self.assertEqual(noneObj.id, 1)

    def testToJsonMethodyNone(self):
        res = Base.to_json_string(None)
        self.assertEqual("[]", res)

    def testToJsonMethodEmpty(self):
        res = Base.to_json_string([])
        self.assertEqual("[]", res)

    def testToJsonMethodCorrect(self):
        r1 = Rectangle(10, 7, 2, 8, 10)
        res1 = '[{"x": 2, "y": 8, "id": 10, "height": 7, "width": 10}]'
        dictr1 = r1.to_dictionary()
        res2 = [dictr1]
        res = Base.to_json_string(res2)
        self.assertEqual(res1, res)
