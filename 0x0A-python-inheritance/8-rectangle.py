#!/usr/bin/python3

"""Creating a class that inherits from another class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle through BaseGeometry"""

    def __init__(self, width, height):
        """Rectangular class derived from BaseGeometry class
        Args:
            width: The width of the rectangular validated by integer_validator.
            height: The height of the rectangle validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
