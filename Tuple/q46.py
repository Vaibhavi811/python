# Convert tuple into a list and remove duplicates
t=(45,77,18,33,33,18,9,5)

# list1= list(set(t))
# print(list1)

list1=[]
for i in t:
    if(i not in list1):
        list1.append(i)
print(list1)
