#!/usr/bin/python3

"""writes a string to a file and returns number of characters written"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open("my_first_file.txt", "w") as filename:
        filename.write(text)
