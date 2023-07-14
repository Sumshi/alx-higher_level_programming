#!/usr/bin/python3

"""defines a class square that inherits from rectangle class"""


Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """ rectangle is the parent(base) class"""
    def __init__(self, size, x=0, y=0, id=None):
        """gives the height and width as size to the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string representation"""
        return ("[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
