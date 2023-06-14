#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []  # to store square matrix
    for row in matrix:  # iterates over row
        new_row = []  # stores the square of rows
        for num in row:  # gets the square of each number
            new_row.append(num ** 2)  # puts the result in new row
        new_matrix.append(new_row)  # new matrix contains squared nums
    return new_matrix
    # return list([num * num for num in row] for row in matrix)
