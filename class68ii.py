import re
# str="xyz"
# pattern="[abc]"
# pattern="[a-z]"
# str="12348745"
# pattern="[0-9]"
# pattern="[a-zA-Z]"
# pattern="[a-zA-Z0-9]"
# str="abcAbC1234"
# pattern="[a-zA-Z0-9]"
# str="23432"
# pattern="\d" #digit
# str="abc"
# pattern="\D" #non digit
# pattern="\w" #word character or special character
# str="abc@123"
# pattern="\W" #non word character or special character
# []set
# \d sequence digit
# \D sequence non digit
# str="Hello"
# pattern="He...o" #3 dots means 3 characters
# pattern="\s" #space
str="hello how are you"
# pattern="^hello"
# pattern="you$" #end with hello
pattern="^hello.*you$" #start and end with hello
flag=re.search(pattern,str) #search
if flag:
    print("valid Email")
else:
    print("Invalid Email")
# print(flag)