# Write a Program to replace whitespaces with an underscore and vice versa.
import re
text="Python Programming Language"
result1=re.sub(r'\s+', '_', text)
print(result1)

result2=re.sub(r"_"," ",result1)
print(result2)