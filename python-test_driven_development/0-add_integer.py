#!/usr/bin/python3
"""
This module contains a method that calculates the sum of two values.
The method, add_integer, takes two arguments, a and b, and ensures that
they are both valid integer or float values. If either a or b is a float, 
it is casted to an integer before performing the addition.
The method then returns the integer sum of a and b.
"""


def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
