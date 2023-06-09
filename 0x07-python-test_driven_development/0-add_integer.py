#!/usr/bin/python3

"""This function adds two integers"""


def add_integer(a, b=98):
    """
    Args:
        a(int or float) the first value
        b(int or float) the second value

    Return: the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
