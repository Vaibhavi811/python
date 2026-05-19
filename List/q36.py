# wap to check all elements are unique or not in list
list= [2,2,8,8,11]
list1=set(list)
print(list1)
if(len(list)==len(list1)):
    print("all elements in list are unique")
else:
    print("Not unique")