#!/usr/bin/python3

"""Write a class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """defines a class"""
    def area(self):
        """initializes object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# print(help(BaseGeometry))
