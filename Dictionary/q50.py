# Write a Program to create a dictionary from a sequence
keys= ["name", "age","id","ph no"]
value= 0
student= dict.fromkeys(keys, value)

for key,value in student.items():
    print(key,":", value)