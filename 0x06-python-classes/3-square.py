#!/usr/bin/python3
"""This is used to define a class square."""


class Square:
    """This is used to represent a square."""

    def __init__(self, size=0):
        """This is used to initialize a new square.
        Args:
            size (int): The size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This return the current area of the square."""
        return (self.__size * self.__size)
