# 1st import the module
import mysql.connector

# 2nd: connect to database, both lines of code down below is necessary

cnx = mysql.connector.connect(user='...', host='127.0.0.1', password='...')

cursor = cnx.cursor()

# 3rd: write sql code: 
make_database = "create database name_of_database"

# 4th: execute sql command
cursor.execute(make_database)
