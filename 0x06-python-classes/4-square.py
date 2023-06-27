#!/usr/bin/python3

"""defines a square """


class Square:
    """initializes a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """defines a getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """defines a setter that allows modifying value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # sets the value of size

    def area(self):
        """calculates the area of the square"""
        return self.__size * self.__size
