#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            element = element + 1
        except IndexError:  # index out of range error
            break
    print("")
    return element
