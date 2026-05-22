#  Write a Program to find the sum of elements of a list using lambda function 
list1= [1,2,3,4,5]
a= lambda c,d: c+d
sum=0

for i in list1:
    sum= a(sum,i)
print(sum)
