#!/usr/bin/python3
"""
   Filter states by Input safer.

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
    query = (
        """SELECT *
            FROM states
            WHERE name=%s
            ORDER BY id ASC;
        """
    )

    cur.execute(query, (argv[4],))
    elems = cur.fetchall()
    for elem in elems:
        print(elem)

    cur.close()
    db.close()
