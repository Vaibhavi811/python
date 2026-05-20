# wap to find the max and min k elements in a tuple
tuple= (23,67,89,54,33,7,11,28,17) 
k= int(input("enter the range:"))

# list= list(tuple)
# print(list)

# list.sort()
# print(list)

list= sorted(tuple)
print(list)

print("min k elements:",list[:k])
print("max k elements:",list[-k:] )