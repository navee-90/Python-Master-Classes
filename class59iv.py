import os
import pickle
os.chdir("N:/temp")
with open("myfile4.pkl","r")as file:
    data=file.read()
    print(data)
