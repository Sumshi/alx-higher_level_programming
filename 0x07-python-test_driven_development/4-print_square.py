#!/usr/bin/python3

"""This function prints the size of a square"""


def print_square(size):
    """
    Args:
    size: must be an integer
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an intege")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
