#!/usr/bin/python3
"""
    Write a function that reads a
    text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
        Function that opens a file and prints
        the content inside it.
    """
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()
        print(file_content)
