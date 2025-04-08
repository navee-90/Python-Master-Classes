import re
str="xyz@gmail.com, cathy@gmail.com; mnj@gmail.com"
pattern=",|;"
flag=re.split(pattern,str) #split
if flag:
    print("valid Email")
else:
    print("Invalid Email")