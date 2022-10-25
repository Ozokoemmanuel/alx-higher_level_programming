#!/usr/bin/python3

"""Checking of class and or sub-class."""


def is_kind_of_class(obj, a_class):
    """Object is an instance of, or the object is an instance of a class that inherited from, the specified class.
    Args:
        obj: the object.
        a_class: the class.
    Returns:
        True, when neccessary and False likewise.
    """

    if isinstance(obj, a_class):
        return True
    return False
