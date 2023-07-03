#!/usr/bin/python3

"""creates a class that defines a rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """sets private attribute for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets height private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """gets the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
            return string

    def __repr__(self):
        """Returns a string representation that can recreate the object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """instance of rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle where weight==size==height"""
        # return cls(size, size) returns a square with equal width and height
        width = size
        height = size
        return cls(width, height)
