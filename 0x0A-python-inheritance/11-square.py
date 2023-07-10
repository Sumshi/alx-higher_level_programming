#!/usr/bin/python3

"""Write a class Square that inherits from Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from class Rectangle"""
    def __init__(self, size):
        """initializes class attributes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates area"""
        return self.__size * self.__size

    def __str__(self):
        """prints string representation"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
