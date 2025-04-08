# regular expression
# A regular expression is a sequence of characters that forms a search pattern.
# Used for:
# Searching
# Matching
# Replacing text
# Validating inputs (like emails, phone numbers, etc.)

import re

text = "My email is test@example.com"

# Search for 'email'
match = re.search("email", text)
print(match.group())  # email

# Find all words
words = re.findall(r"\w+", text)
print(words)  # ['My', 'email', 'is', 'test', 'example', 'com']

# Replace word
new_text = re.sub("email", "contact", text)
print(new_text)  # My contact is test@example.com
