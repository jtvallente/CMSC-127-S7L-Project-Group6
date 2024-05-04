import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gno8fsbhrtx",
    database="food_review_db"
)

if mydb.is_connected():
    print('Connected to database')
