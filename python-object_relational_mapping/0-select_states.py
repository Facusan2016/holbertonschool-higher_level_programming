#!/usr/bin/python3
"""
    Function that selectes the states from the database.

"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute(
        """SELECT *
            FROM states
            ORDER BY id ASC;
        """
    )
    elems = cur.fetchall()
    for elem in elems:
        print(elem)
