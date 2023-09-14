#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

# code should not be executed when imported
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

# connect to mysqldb server
my_database = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    password=argv[2],
    database=argv[3],
    port=3306
)

# define cursor used to execute mysql queries
my_cursor = my_database.cursor()

# execute a select query to select data
my_cursor.execute(
    "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;"
    )

# fetch the data from the query in tuple form
my_data = my_cursor.fetchall()

# iterate through the fetched data and print each row
for row in my_data:
    print(row)

# finally close the cursor
my_cursor.close()
