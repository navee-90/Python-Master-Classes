import os
import pickle
os.chdir("N:/temp")
txt=input("Enete Data: ")
f=open("myfile4.pkl","wb")
pickle.dump(txt,f)