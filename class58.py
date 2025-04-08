import os
folders=os.listdir("N:/")
while True:
    for i in folders:
        print(i)
    ch=input("Enter Folder Name: ")
    print(os.listdir(f"N:/{ch}"))
    choice=input ("Do you want to continue? (yes/no): ")
    if choice=="yes":
        continue
    else:
        break
