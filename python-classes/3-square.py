#!/usr/bin/python3

"""
A class that defines a square
"""

class Square:
    """Initializes a Square instance with a given size"""

    def __init__(self, size=0):
        """__size (int): The size of the square (private)"""
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """define area method, evaluate square area"""
        return self.__size ** 2
