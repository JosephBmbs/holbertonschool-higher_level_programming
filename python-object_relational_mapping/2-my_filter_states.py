#!/usr/bin/python3
"""
A script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__": 

        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name_searched>")
else:
        username, password, database, state_name = argv[1:]
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
