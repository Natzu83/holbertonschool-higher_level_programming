#!/usr/bin/python3
""" A script that lists all states from the database """

# Import the necessary modules
import MySQLdb
import sys

# Check if the script is being executed directly
if __name__ == '__main__':
    # Get the username, password, and database name from the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database using the provided credentials
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SELECT query to retrieve all rows from the 'states' table, ordered by 'id' in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query and store them in the 'rows' variable
    rows = cursor.fetchall()

    # Loop through the rows and print each one
    for row in rows:
        print(row)

    # Close the cursor and database connection to free up resources
    cursor.close()
    db.close()