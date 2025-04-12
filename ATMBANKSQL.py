import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
)
store=mydb.cursor()
store.execute("create database atmbank")
store.execute("use atmbank")
store.execute("create table users(uno int(4),account_no int(12),uname varchar(20),password varchar(12),email varchar(20),phone int(10))")
while True:
    id=int(input("Eneter uno: "))
    account_no=int(input("Eneter Account Number: "))
    uname=input("Enter Username: ")
    password=input("Enter Password:")
    email=input("Enter Email: ")
    phone=int(input("Enter phone: "))
    sql="insert into users(uno,account_no,uname,password,email,phone)values(%s,%s,%s,%s,%s,%s)"
    values=(id,account_no,uname,password,email,phone)
    store.execute(sql,values)
    mydb.commit()
    print(store.rowcount,"record inserted.")
    ch=input("Do you want to continue? (y/n)")
    if ch=='n':
        break
mydb.close()