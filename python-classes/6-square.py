#!/usr/bin/python3

"""
Access and update private attribute, Printing a square
"""


class Square:
    """define variables and methods"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """define area method, evaluate square area"""
        return self.__size ** 2

    def my_print(self):
        """define my_print method, printing of a square"""
        if self.__size == 0:
            print('')
        else:
            for _ in range(self.__position[1]):
                print('')
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

