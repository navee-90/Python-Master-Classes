import os
os.chdir("N:/temp")
name=input("Enter your name:")
age=input("Enter your age:")
city=input("Enter your city:")
f=open("myfile.txt","w")
f.write(f"Name:{name}\nAge:{age}\nCity:{city}")
f.close()