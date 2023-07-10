#!/usr/bin/python3

"""Write a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialises class attributes"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
