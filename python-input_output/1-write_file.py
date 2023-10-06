#!/usr/bin/python3
"""
    Write a function that writes a string to a
    text file (UTF8) and returns the number
    of characters written:
"""


def write_file(filename="", text=""):
    """
        Function that opens a file and writes
        the content inside it.
    """
    with open(filename, "w", encoding="utf-8") as f:
        char_wrt = f.write(text)
        return char_wrt
