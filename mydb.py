import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
)

#create cursor
cursorObject = database.cursor()

cursorObject.execute("create database dtDB")

print('DATABASE created')