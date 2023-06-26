#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # to store the result
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:  # element is not an integer or float
            print("wrong type")
            div = 0
        except ZeroDivisionError:  # division can’t be done
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
