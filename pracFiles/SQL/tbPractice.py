# this code will help get accustomed to using tables in sql
import sqlite3

# Connecting to sqlite connection object
connection_obj = sqlite3.connect('table.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
table = """ CREATE TABLE GEEK (
			email VARCHAR(255) NOT NULL,
			fName CHAR(25) NOT NULL,
			lName CHAR(25),
			score INT
		); """

cursor_obj.execute(table)

cursor_obj.execute('''INSERT INTO GEEK VALUES ('geek1@gmail.com', 'chima', 'ug', 23)''')
cursor_obj.execute('''INSERT INTO GEEK VALUES ('geek2@gmail.com', 'chimaaaa', 'ugwuegbu', 24)''')
cursor_obj.execute('''INSERT INTO GEEK VALUES ('geek3@gmail.com', 'chimaaaaa', 'ugwuegbulam', 25)''')

print("Table is Ready")

print('Data inserted into the table')
data = cursor_obj.execute('''SELECT * FROM GEEK''')
for row in data:
    print(row)

connection_obj.commit()
# Close the connection
connection_obj.close()
