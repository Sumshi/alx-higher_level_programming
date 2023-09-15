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
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC;"
    my_cursor.execute(query, (argv[4],))
    my_data = my_cursor.fetchall()
    if len(my_data) == 0:
        print()
    else:
        tup = ()
        for row in my_data:
            tup += row
        for i in range(len(tup)):
            if i == len(tup) - 1:
                print(tup[i])
            else:
                print(tup[i], end=", ")

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_database.close()
