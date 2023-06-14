#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_score = 0
    total_weight = 0
    for tup in my_list:
        total_score = total_score + tup[0] * tup[1]  # score * weight
        total_weight = total_weight + tup[1]
    return total_score / total_weight
    # products = list(map(lambda x: x[0] * x[1], my_list))  # score * weight
    # weights = list(map(lambda x: x[1], my_list))  # gets weight only
    # return sum(products) / sum(weights)
