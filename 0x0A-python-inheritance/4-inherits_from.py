#!/usr/bin/python3

"""Checking the manner of inheritance."""


def inherits_from(obj, a_class):
    """Checks for the manner of inheritance.
    Args:
        obj: the object.
        a_class: the class.
    Returns:
        True when neccessary and false likewise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
