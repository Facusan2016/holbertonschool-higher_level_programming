#!/usr/bin/python3

import unittest
from models.base import Base

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
