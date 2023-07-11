#!/usr/bin/python3

"""write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads contents of a file"""
    with open("my_file_0.txt", "r") as filename:
        for line in filename:
            print(line, end='')
