#!/usr/bin/python3

"""write a function mylist that inherits from builtin list"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """all elements of list are type int"""
        print(sorted(self))
