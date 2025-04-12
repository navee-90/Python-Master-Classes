import mysql.connector
mydb=mysql.connector.connect(
    host='loacalhost',
    user='root',
    password='root',
    database='mypythondb'
)
mycursor=mydb.cursor()
sql="insert into customers(sno,c_name,email,phone)values(%s,%s,%s,%s)"
values=(1,'Navin','mnj@gmail.com',5675434429)
mycursor.execute(sql,values)
mydb.commit()
print(mycursor.rowcount,"resord inserted.")