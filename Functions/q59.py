# WAP to Invert a Dictionary i.e swap key and values (assume Values are Unique)
dict= {"a":22, "b":11, "c":5}
dict1={}

for key,value in dict.items():
    dict1[value]= key

print("Inverted dictionary:", dict1)