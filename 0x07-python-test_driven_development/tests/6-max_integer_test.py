#!/usr/bin/python3
""" Unittest for the max_integer module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Testcase for the max_integer function"""

    def test_empty_list(self):
        """ Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_at_the_end(self):
        """Test a list where max value is at the end"""
        max_at_the_end = [20, 30, 40, 50]
        self.assertEqual(max_integer(max_at_the_end), 50)

    def test_max_at_begginning(self):
        """Test a list where max value is at the beginning"""
        max_at_beginning = [50, 40, 30, 20]
        self.assertEqual(max_integer(max_at_beginning), 50)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_unique_element_list(self):
        """Test a list with a single element."""
        unique_element = [23]
        self.assertEqual(max_integer(unique_element), 23)

    def test_ints_and_floats_list(self):
        """Test a list of ints and floats."""
        ints_and_floats = [3.53, 19.7, 2, -6]
        self.assertEqual(max_integer(ints_and_floats), 19.7)

    def test_float_list(self):
        """Test a list of floats."""
        float = [8.53, 6.3, -1.23, 19.2, 6.0]
        self.assertEqual(max_integer(float), 19.2)

    def test_string_list(self):
        """Test a string."""
        string = "Sumaya"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings"""
        strings = ["maya", "is", "my", "friend"]
        self.assertEqual(max_integer(strings), "my")

    def test_neg_float_list(self):
        """Test negative floats"""
        neg_float = [-4.35, -89.38, -120.1]
        self.assertEqual(max_integer(neg_float), -4.35)

    def test_diff_datatypes(self):
        """ Test different data types"""
        with self.assertRaises(TypeError):
            max_integer([1, "1"])

    def test_list_list(self):
        """ Test nested list"""
        list = [[1, 2], [2, 1]]
        self.assertEqual(max_integer(list), [2, 1])


if __name__ == "__main__":
    unittest.main()
