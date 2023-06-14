#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  # checks if key is present
        del(a_dictionary[key])  # if key if found, deletes it
    return a_dictionary  # returns modified directory
