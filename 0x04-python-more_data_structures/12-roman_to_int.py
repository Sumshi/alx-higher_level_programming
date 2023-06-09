#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0  # holds the converted integer
    prev_value = 0  # keeps track of previous value

    for char in reversed(roman_string):
        value = numerals[char]

        if value < prev_value:
            result = result - value
        else:
            result = result + value

        prev_value = value

    return result
