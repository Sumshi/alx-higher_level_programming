#!/usr/bin/python3
"""python class to json function"""


def class_to_json(obj):
    """
    function that returns the dictionary description
    for JSON serialization of an object
    args:
    obj which is an instance of a class
    """
    return (obj.__dict__)
