#!/usr/bin/python3

"""This function divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Args:
    matrix: a list of lists of integers or floats
    div: a number(integer or float)

    Return: a new matrix
    """

    if type(matrix) is not list or any(type(row) is not list for row in matrix):
        raise ValueError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
