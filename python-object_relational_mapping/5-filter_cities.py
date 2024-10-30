#!/usr/bin/python3
"""Script that lists all cities of a state"""
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

    # Execute query with safe parameter for state name
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    # Fetch results and format output
    cities = cursor.fetchall()
    print(", ".join([city[0] for city in cities]))

    # Close cursor and database
    cursor.close()
    db.close()