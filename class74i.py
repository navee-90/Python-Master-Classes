# create database
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root' 
)
mycursor=mydb.cursor()
# mycursor.execute("create database mypythondb")
mycursor.execute("create database if not exists mypythondb")
