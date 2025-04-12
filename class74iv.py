import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mypythondb'
)
mycursor=mydb.cursor()
while True:
    id=int(input("Enter sno: "))
    name=input("Eneter Name: ")
    email=input("Eneter Email: ")
    phone=input("Enter Phone: ")
    sql="insert into customers(sno,c_name,email,phone) values(%s,%s,%s,%s)"
    values=(id,name,email,phone)
    mycursor.execute(sql,values)
    mydb.commit()
    print(mycursor.rowcount,"record inserted.")
    choice=input("Do You Want to continue? (y/n)")
    if choice=='n':
        break