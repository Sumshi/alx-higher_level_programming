#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:  # list is empty
        return None
    else:  # list not empty
        max = my_list[0]  # max is initialized to first element in list
        for num in my_list:  # iterates through each element
            if num > max:  # compares each element with current max value
                max = num
        return max
