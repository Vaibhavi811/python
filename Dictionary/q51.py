# Write a Program to generate dictionary of numbers and their squares (i, i*i) from 1 to N
n= int(input("Enter the value of n:"))
dic= {}

for i in range(1,n+1):
    dic[i]= i*i
print(dic)