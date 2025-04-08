import os
folders=os.listdir("N:/")
for i in folders:
    print(i)
ch=input("Enter folder name: ")
print(os.listdir(f"N:/{ch}"))

file=os.listdir("N:/temp")
print(file)