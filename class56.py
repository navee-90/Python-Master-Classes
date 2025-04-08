import os
print("*** File Management ***")
os.chdir("N:/temp")

print("1.Wrire a file")
print("2.Reacd a file")
print("3.Delete a file")
ch=input("Enter your choice: ")
if ch=="1":
    f=open("myfile2.txt","w")
    data=input("Enter Data: ")
    f.write(data)
    f.close()
elif ch=="2":
    f=open("myfile2.txt","r")
    data=f.read()
    print(data)
    f.close()
elif ch=="3":
    os.remove("myfile2.txt")
    print("File deleted successfully")
else:
    print("Invalid choice")