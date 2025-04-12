import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mypythondb'
)
mycursor=mydb.cursor()
mycursor.execute("create table customers(sno int(5),c_name varchar(15),email varchar(20),phone int(10))")