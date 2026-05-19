# wap to find the cumulative sum of elements of a list
list= [10,20,30,40]
sum=0
cum_list=[]
for i in list:
    sum+=i
    cum_list.append(sum)
print(sum)
print(cum_list)