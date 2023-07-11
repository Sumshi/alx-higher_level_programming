#!/usr/bin/python3

"""Student to JSON"""


class Student:
    def __init__(self, first_name, last_name, age):
        """defines a class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return (self.__dict__)
