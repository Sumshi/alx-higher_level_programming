#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:  # list is empty
        return None
    else:  # list not empty
        my_list.sort()  # sorts list in ascending order
        max_value = my_list[-1]  # last value
    return my_list

max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
