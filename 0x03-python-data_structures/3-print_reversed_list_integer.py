#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:  # checks if list is empty or not
        my_list.reverse()  # list not empty, reverse
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
