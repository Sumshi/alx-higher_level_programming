#!/usr/bin/python3

"""defines a square"""


class Square:
    """initializes a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """defines a getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """defines a setter for position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area"""
        return self.__size * self.__size

    def my_print(self):
        """prints # to the stdout"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)         
