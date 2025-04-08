import os
os.chdir("N:/temp")
while True:
    name=input("Enter Name: ")
    age=input("Enter age: ")
    city=input("Enter city: ")
    f=open("myfile1.txt","w")
    f.write(f"Name:{name}\nAge:{age}\ncity:{city}")
    ch=input("Do you want to continue? (y/n): ")
    if ch=="y":
        continue
    else:
        break
f.close()