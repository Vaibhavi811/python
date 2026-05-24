# wap that takes a string containing multiple phone numbers and uses regular expressions to extract all valid 10 digit numbers.
import re
numbers= "MY numbers are 8112210059, 123456789, 7852004598, 9462394190"
pattern= r"(\b\d{10}\b)"
match= re.findall(pattern,numbers)

for num in match:
    print(num)