# The re module stands for regular expression and is part of Python's standard library.

# It provides functions to:
# Search for patterns in text
# Match specific string formats (like email, phone numbers, etc.)
# Replace text
# Extract data based on patterns

import re
str="username2345@gmail.com"
pattern="@"
flag=re.search(pattern,str) #search
if flag:
    print("valid Email")
else:
    print("Invalid Email")