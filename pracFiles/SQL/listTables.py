# this pulls all created tables from an already created .db file [VERY USEFUL]

import sqlite3

try:
    # this is where the connection is established
    con = sqlite3.connect('hotel_data.db')
    print('SQLite connection established')

    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

    cur = con.cursor()

    cur.execute(sql_query)

    # printing out all of the tables
    print('List of tables')
    print(cur.fetchall())

finally:

    if con:
        con.close()
        print('The SQL connection is closed.')
