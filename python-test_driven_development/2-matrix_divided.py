#!/usr/bin/python3

"""
Module 2-matrix_divided
This module contains a method that divides all elements of a matrix
and returns a new matrix.The method, matrix_divided, takes two arguments:
matrix and div. The matrix should be a list of lists, where each inner list contains
integers or floats. The div should be a non-zero integer or float that will be used as
the divisor for all elements in the matrix.
"""


def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
            or not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]

    return result
