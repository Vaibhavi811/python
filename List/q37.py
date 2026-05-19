# wap to replace list item with new value if found
list=[10,20,30,40,50]

if(30 in list):
    index= list.index(30)
    list[index]= 60
    print(list)
else:
    print("Not found")