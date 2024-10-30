#!/usr/bin/python3
"""Script that lists all cities from the database"""
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

    # Execute query to join cities and states
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch and print results
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close cursor and database
    cursor.close()
    db.close()