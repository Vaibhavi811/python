# 1.Write a Program that matches a string that has an a followed by zero or more b's 
import re
text=["a","abb","abbbb","abbbbc","abbb"] 
pattern1=r'^ab*$'
for i in text:
    if re.match(pattern1,i):
        print(i)

print(" ")
# 2. Write a Program that matches a string that has an a followed by one or more b's  
pattern2=r'^ab+$'
for i in text:
    if re.match(pattern2,i):
        print(i)

print(" ")
# 3. Write a Program that matches a string that has an a followed by three 'b'
pattern3= r'^abbb$'
for i in text:
    if re.match(pattern3,i):
        print(i)