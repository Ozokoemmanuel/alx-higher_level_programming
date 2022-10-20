#!/usr/bin/python3
"""Module of addition for testing"""


def add_integer(a, b=98):
    """Adds the integers
        Arguments:
        @a: first integer
        @b: second integer, default is 98
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
