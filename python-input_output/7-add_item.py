#!/usr/bin/python3

from sys import argv
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

"""
    Write a script that adds all arguments to a Python list
    and then save them to a file:
"""


if __name__ == "__main__":
    """Main Function"""

    fileName = "add_item.json"
    try:
        with open(fileName, "r") as f:
            if f.read() == "":
                save_json([], fileName)
    except Exception:
        save_json([], fileName)

    data = load_json(fileName)
    for i in range(1, len(argv)):
        data.append(argv[i])

    save_json(data, fileName)
