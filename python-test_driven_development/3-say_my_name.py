#!/usr/bin/python3
"""
    Module that defines the say_my_name
    function that prints the first and last name.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the first and the last name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("{:s} {:s}".format(first_name, last_name))
