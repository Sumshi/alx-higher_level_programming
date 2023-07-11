#!/usr/bin/python3

"""creates an Object from a “JSON file"""

import json
"""uses json file"""


def load_from_json_file(filename):
    """
    function that parses json data from file to python object:
    """
    with open(filename, 'r') as file:
        json.load(file)
