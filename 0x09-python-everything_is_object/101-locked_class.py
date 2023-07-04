#!/usr/bin/python3
"""creates a class with no class or object attribute"""


class LockedClass:
    """slot is used to restrict the creation of instance attributes
    to only the ones listed
    In this case, we list first_name as the only allowed attribute.
    """

    __slots__ = ['first_name']
