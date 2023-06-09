#!/usr/bin/python3

"""defines a class rectangle that inherits from base class"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # id is defined in the base class
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """defines private attribute for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defines private attribute for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """defines private attribute for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the attribute for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """defines private attribute for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the attribute for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of a rectangle"""
        return (self.__width) * (self.__height)

    def display(self):
        """prints # to the stdout"""
        for _ in range(self.__y):  # handles for y axis
            print()
        for _ in range(self.__height):  # handles for x axis
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """prints string representation of rectangle"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:  # if args is present
            attributes = ['id', 'width', 'height', 'x', 'y']
            for index, arg in enumerate(args):
                setattr(self, attributes[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
