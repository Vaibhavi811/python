# wap to interchange first and last variable in list
list= [10,20,30,40,50,60]

# list[0],list[-1] = list[-1],list[0]
# print(list) 

list[0]=10
list[-1]=60
list[-1]= list[-1]-list[0]
list[0]= list[0]+list[-1]
list[-1]= list[0]-list[-1]
print(list)
