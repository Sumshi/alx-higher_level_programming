#!/usr/bin/python3

"""python object to json string"""
import json
"""json module is imported"""


def to_json_string(my_obj):
    """converts python object json string"""
    return json.dumps(my_obj)
