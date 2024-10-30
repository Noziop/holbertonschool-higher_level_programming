#!/usr/bin/python3
"""Script that is safe from MySQL injections"""
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

    # Use parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM states \
                   WHERE name = %s \
                   ORDER BY id ASC", (sys.argv[4],))

    # Fetch and print results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and database
    cursor.close()
    db.close()