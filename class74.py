# class 13
# MySQL
# To use MySQL in Python, you need to connect Python to your MySQL database using a connector library like mysql-connector-python or PyMySQL.
# pip install mysql-connector-python or python3.11 -m pip install mysql-connector-python
# import mysql.connector

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydata'
)
mycursor=mydb.cursor()
mycursor.execute("select*from student")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
