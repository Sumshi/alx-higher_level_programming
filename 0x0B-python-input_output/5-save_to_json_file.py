#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """converts python object to json and save it in text file"""
    with open(filename, 'w') as file:
        json.dumps(my_obj, file)
