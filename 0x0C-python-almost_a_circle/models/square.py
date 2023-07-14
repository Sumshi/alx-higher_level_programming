#!/usr/bin/python3
"""defines a class square that inherits from rectangle class"""
from models.square import Square


class Square(Rectangle):
    """ rectangle is the parent(base) class"""
    def __init__(self, size, x=0, y=0, id=None):
        """gives the height and width as size to the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns string representation"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
