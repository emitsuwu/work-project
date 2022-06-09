# importing sqlite3 module
import sqlite3

# create connection by using object to connect with hotel_data database
connection = sqlite3.connect('hotel_data.db')


# insert query to insert food details in the above table
connection.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )");
connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )");
connection.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )");


print("Food id and Food Name\n")

# create a cousor object for select query
cursor = connection.execute("SELECT FIND, FNAME from hotel ")

# display all data from FOOD1 table
for row in cursor:
	print(row)
