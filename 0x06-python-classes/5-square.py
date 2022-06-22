#!/usr/bin/python3
"""This is used to define a class square."""


class Square:
    """This is used to represent a square."""

    def __init__(self, size):
        """This is used to initialize a new square.
        Args:
            size (int): The size of a new square.
        """
        self.size = size

    @property
    def size(self):
        """This is used to get/set the current size of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This is used to Return the current area of a square."""
        return (self.__size * self.__size)

    def my_print(self):
        """This is used to print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
