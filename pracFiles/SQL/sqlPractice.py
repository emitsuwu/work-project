# this program will help me get acquainted with sqlite3

import sqlite3

try:

    # this creates the SQL connection, cursor, and prints 'Database Initialization' to the console...?
    sqliteConnection = sqlite3.connect("sql.db")
    cursor = sqliteConnection.cursor()
    print("Database Initialization")

    # This creates a SQL query and executes said query
    query = "select sqlite_version();"
    cursor.execute(query)

    # This fetches the result of the query, and outputs the result
    result = cursor.fetchall()
    print("SQLite Version is {}".format(result))

    # this closes the cursor | THIS IS IMPORTANT AND SHOULD BE DONE MOST OF THE TIME!!!
    cursor.close()

# error handler
except sqlite3.error as error:
    print("Error occured - ", error)

# close db connection irrespective of success or failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite connection closed.")
