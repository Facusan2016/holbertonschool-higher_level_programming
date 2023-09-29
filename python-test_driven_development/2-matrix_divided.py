#!/usr/bin/python3
"""
    This module defines an divide matrix function
    and it's tested on /tests folder.

"""


def matrix_divided(matrix, div):
    """
    Divides each element of the matrix by div
    """
    err_m = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list):
        raise TypeError(err_m)

    if all(not isinstance(row, list) for row in matrix):
        raise TypeError(err_m)

    row_len = len(matrix[0])
    for row in matrix:
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(err_m)
        if len(row) != row_len:
            msg = 'Each row of the matrix must have the same size'
            raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    n_matrix = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return n_matrix
