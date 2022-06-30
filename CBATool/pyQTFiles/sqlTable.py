# this is the file that will be used as an example for the CBA tool

import sqlite3

# Connecting to sqlite3
connection = sqlite3.connect('sqlTable.db')

# create cursor object
cursor = connection.cursor()

    # Drop the VENDOR table if already exists | makes life easier when running this file multiple times for debugging
cursor.execute("DROP TABLE IF EXISTS VENDOR")

# creating table VENDOR
table = """ CREATE TABLE VENDOR (
                Price real,
                Amt INT
            ); """

cursor.execute(table)


# Inserting dummy data into VENDOR table
def insertData(x, y):

    # inserts data given from cba GUI
    connection.execute(
    """INSERT INTO VENDOR (Price, Amt) VALUES (?, ?)""", (x, y))

    # save the changes made to the table
    connection.commit()


# test to make sure that table is created and can display correctly
def checkData():
    data = cursor.execute("""SELECT * FROM VENDOR""")
    print()
    print("Vendor table: ")
    for row in data:
        print(row)

def conClose():
    # this closes the connection
    connection.close()
