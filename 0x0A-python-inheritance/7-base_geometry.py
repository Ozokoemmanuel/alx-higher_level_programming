#!/usr/bin/python3

"""An empty base geometry."""


class BaseGeometry:
    """Represents the base geometry."""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value.
        Args:
            name: the name.
            value: the value.
        Returns:
            It has no returns
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater then 0")
