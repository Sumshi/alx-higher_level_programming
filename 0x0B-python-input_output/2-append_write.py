#!/usr/bin/python3

""" appends a string to a text file and returns no of characters added"""


def append_write(filename="", text=""):
    """appends to a file"""
    with open(filename, 'a') as file:
        return file.write(text)
