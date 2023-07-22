# Install mysql
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="password123",
)
# Prepare cursor object
cursor = db.cursor()

# Create a database

cursor.execute("CREATE DATABASE portfolio")

print("Initialized the database")