#!/usr/bin/python3
"""Script that lists all states from the database"""
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

    # Execute the query to get all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()