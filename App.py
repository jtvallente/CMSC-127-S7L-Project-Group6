import mysql.connector
from connector import mydb
from library import main


print("Running the Food Review App...")

# Close the database connection
if mydb.is_connected():
    print('Connected to database')
else:
    print('Failed to connect to database')

    import mysql.connector

# Create a cursor object using the connection
mycursor = mydb.cursor()


#This is just a sample logic for the main file
# Define the query to select all rows from the 'users' table
query = "SELECT * FROM Users"

# Execute the query
mycursor.execute(query)

# Fetch all the rows from the result
rows = mycursor.fetchall()

# Print the rows
for row in rows:
    print(row)


#Entry point
main.entry_point()

# Close the cursor and connection
mycursor.close()
mydb.close()


