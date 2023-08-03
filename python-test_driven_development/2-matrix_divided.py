#!/usr/bin/python3
"""A function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
            or not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    result = [[round(element / div, 2) for element in row] for row in matrix]

    return result
