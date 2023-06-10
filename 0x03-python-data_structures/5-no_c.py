#!/usr/bin/python3
def no_c(my_string):
    new_string = ''  # empty string
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string = new_string + char
# each letter is added to the new string except cC
    return new_string
