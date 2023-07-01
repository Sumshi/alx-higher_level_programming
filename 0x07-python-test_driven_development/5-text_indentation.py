#!/usr/bin/python3

"""Prints text indented"""


def text_indentation(text):
    """
    Args:
    text: must be a string

    Raises:
    TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    result = ""  # will store the modified test
    for char in text:  # iterates over each character in text
        result += char  # appends each character to result
        if char in ['.', '?', ':']:
            result += '\n\n'
    print(result.strip())
