#!/usr/bin/python3

""" inserts a line of text to a file containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as file:
        lines = file.read()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in lines:
                file.write(new_string)
        file.truncate()
