import os
os.chdir("N:/temp")
f=open("myfile.txt","a") # a means append line
f.write("\n this second line")
f.close()