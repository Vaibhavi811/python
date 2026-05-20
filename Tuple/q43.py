# wap to create a list of tuples from given list having no and its cube in each tuple
list= [2,3,4,5,6]
list1=[]

for i in list:
    list1.append((i,i**3))
print(list1)