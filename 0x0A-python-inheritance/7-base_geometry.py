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
            name (str): the name.
            value (int): the value.
        Raises:
            TypeError: If the value is not an integer.
            Valueerror: If the value <= 0.
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater then 0".format(name))
