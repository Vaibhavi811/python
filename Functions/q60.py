#  WAP to Sort a dictionary in ascending and descending order based on values.
dict1= {"a":22, "b":28, "c":5}

ascending= dict(sorted(dict1.items(), key=lambda x:x[1]))
print("Ascending order:",ascending)

descending= dict(sorted(dict1.items(), key=lambda x:x[1] ,reverse= True))
print("Descending order:", descending)
