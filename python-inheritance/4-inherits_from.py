#!/usr/bin/python3
"""
    Module definition for is_same_class function
    that checks what is mentioned down.

"""


def inherits_from(obj, a_class):
    """
        if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
    """
    if issubclass(type(obj), a_class) and not isinstance(type(obj), a_class):
        return True
    else:
        return False
