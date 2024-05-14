import json
import mysql.connector

# Replace the values with your actual database connection details
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Inloggen01",
    database="mydb"
)

print(mydb)

# Define the SQL query to select all data from the "sporthal" table in the "Basketbal" database
query = 'SELECT * FROM Klanten'

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute the SQL query
mycursor.execute(query)

# Fetch all the results from the executed query
result = mycursor.fetchall()

# Iterate over the results and print each row
for sporthal in result:
    print(sporthal)


print(mycursor.rowcount)

## After you finish working with the database, don't forget to close the connection:
# mydb.close()
