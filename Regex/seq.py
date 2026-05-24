# Write a Program to find the sequences of one upper case letter followed by lower case letters
import re
text= "Python is a Programming Language"

pattern=r"[A-Z][a-z]+"
match= re.findall(pattern,text)

print(match)
