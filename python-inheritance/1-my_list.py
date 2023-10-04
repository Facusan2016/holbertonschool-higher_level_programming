#!/usr/bin/python3
"""
    In this module we define a MyList class
"""


class MyList(list):
    """MyList class definition that inherits form List"""
    def print_sorted(self):
        """Sorts and prints a list."""
        list_copy = self[:]
        print(sorted(list_copy))
