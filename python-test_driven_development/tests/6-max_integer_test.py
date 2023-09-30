#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        ret_val = max_integer([])
        self.assertEqual(ret_val, None)

    def test_simple_case(self):
        ret_val = max_integer([1, 2, 4, 2])
        self.assertEqual(ret_val, 4)

    def test_negative_values(self):
        ret_val = max_integer([-7, -5, -2, 1])
        self.assertEqual(ret_val, 1)

    def test_one_value(self):
        ret_val = max_integer([1])
        self.assertEqual(ret_val, 1)

    def test_max_value_beggining(self):
        ret_val = max_integer([6, 1, 2, 3])
        self.assertEqual(ret_val, 6)
