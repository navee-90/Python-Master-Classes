import re
str="username2345@gmail.com"
pattern="[abc]"
flag=re.search(pattern,str) #search
if flag:
    print("valid Email")
else:
    print("Invalid Email")