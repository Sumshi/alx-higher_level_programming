#!/usr/bin/python3

"""defines a square"""


class Square:
    """initializes a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """defines a getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """defines a setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area"""
        return self.__size * self.__size

    def my_print(self):
        """prints # to the stdout"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
