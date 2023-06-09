#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square"""
        self.size = size

    @property
    def size(self):
        """sets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """retrieves value of private attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """implements equality. compares 2 squares , self and other"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Implements not equal(!=) between squares."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Implements less than operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """implements the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
