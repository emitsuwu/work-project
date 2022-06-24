import sqlite3
from pracFiles.tryExept import start_game
# import pracFiles.tryExcept as jackson
#
#
start_game()


# Connecting to sqlite
connection_obj = sqlite3.connect('alterTable.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the TEST table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS TEST")

# Creating table
table = """ CREATE TABLE TEST (
			Email VARCHAR(255) NOT NULL,
			Name CHAR(25) NOT NULL,
			Score INT
		); """

cursor_obj.execute(table)

# Inserting data into geek table
connection_obj.execute(
	"""INSERT INTO TEST (Email,Name,Score) VALUES ("chima1@gmail.com","Chima1",25)""")
connection_obj.execute(
	"""INSERT INTO TEST (Email,Name,Score) VALUES ("chima2@gmail.com","Chima2",15)""")
connection_obj.execute(
	"""INSERT INTO TEST (Email,Name,Score) VALUES ("chima3@gmail.com","Chima3",36)""")
connection_obj.execute(
	"""INSERT INTO TEST (Email,Name,Score) VALUES ("chima4@gmail.com","Chima4",27)""")
connection_obj.execute(
	"""INSERT INTO TEST (Email,Name,Score) VALUES ("chima5@gmail.com","Chima5",40)""")
connection_obj.execute(
	"""INSERT INTO TEST (Email,Name,Score) VALUES ("chima6@gmail.com","Chima6",14)""")
connection_obj.execute(
	"""INSERT INTO TEST (Email,Name,Score) VALUES ("chima7@gmail.com","Chima7",10)""")

# alter the already created table in several ways
new_column = "ALTER TABLE TEST ADD COLUMN Age int"
cursor_obj.execute(new_column)

# testing to see if the new column is recognized
connection_obj.execute(
    """INSERT INTO TEST (Email, Name, Score, Age) VALUES ("chima8@gmail.com", "Chima8", 16, 45)""")

# deleting an already created row
print('Chima2 is going to be deleted.')
connection_obj.execute("DELETE from TEST WHERE Name='Chima2'")\

# updating a specific column's values
print('Setting the entire Name column to Chima2')
#connection_obj.execute("UPDATE TEST set Name='Chima2'")

# Display table
data = cursor_obj.execute("""SELECT * FROM TEST""")
print('TEST Table:')
for row in data:
	print(row)

connection_obj.commit()

# Close the connection
connection_obj.close()
