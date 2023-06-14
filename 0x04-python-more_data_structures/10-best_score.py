#!/usr/bin/python3

def best_score(a_dictionary: dict):
    if not a_dictionary:  # it is emmpty dictionary
        return None

    best = max(a_dictionary.values())  # gets the maximum value
    for key, value in a_dictionary.items():
        if value == best:
            return key
