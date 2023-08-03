#!/usr/bin/python3
"""A script that lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM the states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
        else:
            pass
    cur.close()
    db.close()
