#!/usr/bin/python3
"""
Square class to define a square
"""
class Square:
    """To initialize the size of the square.
        It must be private though
    """
    def __init__(self, size=0):
        self.__size = size
        
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    """
    To find the area of the square
    """
    def area(self):
        return self.__size ** 2

    @property
    def size(self) -> int:
        """
        Retrive the instance attribute of size
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
        set value size
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
