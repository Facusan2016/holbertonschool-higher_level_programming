#!/usr/bin/python3
"""
    Write a function that appends a string to a
    text file (UTF8) and returns the number
    of characters written:
"""


def append_write(filename="", text=""):
    """
        Function that opens a file and appends
        the content inside it.
    """
    with open(filename, "a", encoding="utf-8") as f:
        char_wrt = f.write(text)
        return char_wrt
