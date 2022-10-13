#!/usr/bin/python3
"""Square class that defines a square"""
class Square:
    """
        Define the properties of a square

    """
    def __init__(self, size=0):
        """
        Innitialize the size of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")

        self.__size = size
