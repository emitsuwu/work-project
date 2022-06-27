# this is the file that will be used as an example for the CBA tool

import sqlite3
from pyQTFiles.cba2.py import setValues
# import logic file here, so it can run and you can get local data to insert into table
# look at G4G article on how to use other .py files' local variables

# Connecting to sqlite3
connection = sqlite3.connect('sqlTable.db')

# create cursor object
cursor = connection.cursor()

# Drop the VENDOR table if already exists | makes life easier when running this file multiple times for debugging
cursor.execute("DROP TABLE IF EXISTS VENDOR")

# creating table VENDOR
table = """ CREATE TABLE VENDOR (
            Name CHAR(255) NOT NULL,
            Price real,
            Amt INT
        ); """

cursor.execute(table)

# Inserting dummy data into VENDOR table
connection.execute(
    """INSERT INTO VENDOR (Name, Price, Amt) VALUES ("Part1", 34.60, 1)""")
connection.execute(
    """INSERT INTO VENDOR (Name, Price, Amt) VALUES ("Part2", 82.50, 3)""")
connection.execute(
    """INSERT INTO VENDOR (Name, Price, Amt) VALUES ("Part3", 24.56, 2)""")
connection.execute(
    """INSERT INTO VENDOR (Name, Price, Amt) VALUES ("Part4", 57.89, 1)""")

# test to make sure that table is created and can display correctly
data = cursor.execute("""SELECT * FROM VENDOR""")
print()
print("Vendor table: ")
for row in data:
    print(row)

# save the changes made to the table
connection.commit()

# close the connection
connection.close()
