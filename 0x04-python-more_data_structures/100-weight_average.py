#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    products = list(map(lambda x: x[0] * x[1], my_list))  # score * weight
    weights = list(map(lambda x: x[1], my_list))  # gets weight only
    return sum(products) / sum(weights)
