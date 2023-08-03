#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>")
    else:
        username, password, database = argv[1:]


        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        cur = conn.cursor()

        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
