#!/usr/bin/python3
"""creates a class with no class or object attribute"""


class LockedClass:
    """slot is used to restrict the creation of instance attributes"""
    __slots__ = ['first_name']
