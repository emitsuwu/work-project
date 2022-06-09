# this sql program helps me get accustomed to how sql datatypes work

# importing sqlite3 to use it
import sqlite3

# creating the sqlite3 connection and cursor
con = sqlite3.connect('data.db')

# creating an exam hall table
con.execute('''CREATE TABLE exhall(NAME TEXT, PIN INTEGER, OCCUPANCY REAL);''')

# inserting data (tuples) into TABLE
con.execute('''INSERT INTO exhall VALUES('hall_a', 8967, 94.2)''')
con.execute('''INSERT INTO exhall VALUES(NULL, 12134, 1.10)''')

# reads out both of the rows that were previously created, as well as their types of data
cur = con.execute('''SELECT * FROM exhall;''')
for i in cur:
    print(str(i[0])+" "+str(i[1])+" "+str(i[2]))
    print(str(type(i[0]))+" "+str(type(i[1]))+" " + str(type(i[2])))
