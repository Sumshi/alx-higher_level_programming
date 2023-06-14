#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # search is element to search, replace element to replace with
    new_list = []
    for element in my_list:  # iterates over all the elements in the list
        if element == search:  # if current element is same as search element
            new_list.append(replace)  # replaces it and puts in new_list
        else:  # if is not egual
            new_list.append(element)  # current element is put
    return new_list
    # new_list = [replace if x == search else x for x in my_list]
