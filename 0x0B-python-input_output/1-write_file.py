#!/usr/bin/python3

"""writes a string to a file and returns number of characters written"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, 'w') as file:
        return file.write(text)
