# THIS IS A FILE THAT IS MERELY MADE FOR TESTING PURPOSES DON'T THINK ANYTHING OF IT

import sqlite3

connection = sqlite3.connect('sqlTable2.db')

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS VENDOR")

table = """ CREATE TABLE VENDOR (
                Price real,
                Amt INT
            ); """

cursor.execute(table)

def insertData():
    connection.execute(
            """INSERT INTO VENDOR (Price, Amt) VALUES (34.60, 1)""")
    connection.execute(
            """INSERT INTO VENDOR (Price, Amt) VALUES (82.50, 3)""")
    connection.execute(
            """INSERT INTO VENDOR (Price, Amt) VALUES (24.56, 2)""")
    connection.execute(
            """INSERT INTO VENDOR (Price, Amt) VALUES (57.89, 1)""")

    connection.commit()


# test to make sure that table is created and can display correctly
insertData()
data = cursor.execute("""SELECT * FROM VENDOR""")
print()
print("Vendor table: ")
for row in data:
    print(row)

# this closes the connection
connection.close()
