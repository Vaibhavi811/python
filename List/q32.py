# wap to demonstrate various list operations.
list=[100,20,50,50,89,56,89,67,50,67]

first_element= list[0]
last_element= list[-1]
print(first_element)
print(last_element)

slice= list[1:3]
print(slice)

list.append(70)
print(list)

list.extend([80,90])
print(list)

list.insert(2,30)
print(list)

list[0]= 1
print(list)

list.remove(50)
print(list)

list.pop()
print(list)

del list[2]
print(list)

length= len(list)
print(length)

list.sort()
print(list)

list.reverse()
print(list)

print(list.count(89))

print(list.index(50))