#!/usr/bin/python3

"""An instance check"""


def is_same_class(obj, a_class):
    """To check if an object is exactly the instance of a class.
    Args:
        obj: THe object
        a_class: The class to check
    Returns:
        True if available, False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
