#!/usr/bin/python3

"""Class that inherits from List"""


class MyList(list):
    """The sub-class MyList that inherits from base list List"""

    def print_sorted(self):
        """Prints the sorted list
        """
        print (sorted(self))
