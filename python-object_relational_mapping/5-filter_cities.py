#!/usr/bin/python3
"""
  All cities by state.

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
        """
            SELECT name
            FROM cities
            WHERE cities.state_id = (
                SELECT id
                FROM states
                WHERE states.name = %s
            );
        """
    )

    cur.execute(query, (argv[4],))
    elems = cur.fetchall()
    printArr = []

    for elem in elems:
        printArr.append(elem[0])

    print(*printArr, sep=', ')

    cur.close()
    db.close()
