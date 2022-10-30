#!/usr/bin/python3

"""subclass from a class."""

Rectangle = __import__('9-rectangle').Rectangle

"""Creating a square from a rectangle."""


class Square(Rectangle):
    """Defining the square representing the rectangle."""

    def __init__(self, size):
        """Representing the square.
        Args:
            size: The lenght of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
