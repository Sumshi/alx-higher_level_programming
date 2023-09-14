#!/usr/bin/python3
"""
lists all states and cities from the database hbtn_0e_0_usa
"""

# code should not be executed when imported
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Connect database using command-line arguments
    my_database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

    # Create cursor obj to interact with database
    my_cursor = my_database.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute(
        """SELECT * FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id"""
    )

    print(", ".join([city[2]
                     for city in my_cursor.fetchall()
                     if city[4] == argv[4]])

          )

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_database.close()
