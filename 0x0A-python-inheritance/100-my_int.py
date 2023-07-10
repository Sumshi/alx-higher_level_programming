#!/usr/bin/python3

"""Write a class MyInt that inherits from int:"""


class MyInt(int):
    """myInt inherits from builtin int"""
    def __eq__(self, other):
        """eq represents == (equal) operator"""
        return int(self) != other

    def __ne__(self, other):
        """ne represents != (not equal to)"""
        return int(self) == other
