# re is built in module, In python regular expression is sequence of characters that defines a search pattern.
# validating inputs,extract substrings,replace part of string.
import re
str="hello"
pattern="hello|Namste"
flag=re.search(pattern,str) #search
if flag:
    print("valid")
else:
    print("Invalid")
# print(flag)