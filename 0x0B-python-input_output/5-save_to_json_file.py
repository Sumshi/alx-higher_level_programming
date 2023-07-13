#!/usr/bin/python3

"""Write and convert to a JSON string"""

import json
"""converts python object to json and writes in a text file"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation:
    my_obj is the python oject to serialize to json
    file is the file to write to
    """
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
