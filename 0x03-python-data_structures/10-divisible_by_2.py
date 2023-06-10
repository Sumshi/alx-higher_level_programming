#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []  # empty list to store values
    for num in my_list:  # iterates throught the list
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
