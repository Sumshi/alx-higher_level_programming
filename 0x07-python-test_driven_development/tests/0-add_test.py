#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
add_integer = __import__('0-add_integer').add_integer

class TestAddInteger(unittest.TestCase):
    def test_one(self):
        result = (2, 4)
        self.assertEqual(add_integer(result), 6)

    def test_one(self):
        result = (2, 4)
        self.assertEqual(add_integer(result), 6)
