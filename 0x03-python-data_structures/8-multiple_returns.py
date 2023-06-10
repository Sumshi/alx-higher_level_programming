#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)  # gets length of sentense
    if length == 0:  # length is empty if length == 0
        first_char = None
    else:  # length is not empty
        first_char = sentence[0]
    return (length, first_char)
