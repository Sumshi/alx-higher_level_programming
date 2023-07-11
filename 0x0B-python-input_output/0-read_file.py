#!/usr/bin/python3

"""write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads contents of a file"""
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
