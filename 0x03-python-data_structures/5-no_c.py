#!/usr/bin/python3
def no_c(my_string):
    result = ''  # empty string
    for char in my_string:
        if char != 'c' and char != 'C':
            result = result + char
    return result