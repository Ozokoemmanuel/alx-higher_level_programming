#!/usr/bin/python3
"""Fuction that prints the representation od a square."""


def print_square(size):
    """Prints a square represented by the character #.
    Args:
        size: the size of the square.
    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if float(size) < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
