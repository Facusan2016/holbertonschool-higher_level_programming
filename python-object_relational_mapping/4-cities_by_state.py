#!/usr/bin/python3
"""
  Cities by states.

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
        """SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
        """
    )

    cur.execute(query)
    elems = cur.fetchall()
    for elem in elems:
        print(elem)

    cur.close()
    db.close()
