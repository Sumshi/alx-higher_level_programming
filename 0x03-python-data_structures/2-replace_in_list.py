#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list  # returns original list
    else:
        my_list[idx] = element  # replaces element at an index
        return my_list  # return new list
