#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()  # creates a copy of original list
    if idx < 0 or idx >= len(my_list):  # if index is out of range
        return my_list.copy()
    else:
        copy[idx] = element  # the copy of list is modifies
        return copy  # return new list
