#!/usr/bin/python3

"""A class that inherits from another."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle, a subclass of BaseGeometry."""

    def __init__(self, width, height):
        """Instantiation with the width and height.
        Args:
            width: The width of the rectangle.
            height: the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """The area of the rectangle."""
        return self.__width * self.__height
    
    def __str__(self):
        """Return the print() and str() representation of a rectangle."""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
