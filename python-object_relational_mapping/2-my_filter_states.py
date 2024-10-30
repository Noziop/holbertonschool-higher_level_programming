#!/usr/bin/python3
"""Script that takes argument and lists states"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL with command line arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute query with user input (ATTENTION: SQL Injection possible!)
    cursor.execute("SELECT * FROM states \
                   WHERE name = '{}' \
                   ORDER BY id ASC".format(sys.argv[4]))

    # Fetch and print results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and database
    cursor.close()
    db.close()