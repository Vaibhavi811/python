# wap to demonstrate various tuple operations
tuple= (12,45,63,28,77)
tuple1= (22,17,5,8,11)

first_element= tuple[0]
last_element= tuple[-1]
print(first_element)
print(last_element)

slice= tuple[0:3]
print(slice)

length= len(tuple)
print("Length of tuple", length)

conc= tuple + tuple1
print(conc)

rep= tuple1*2
print(rep)

for i in tuple:
    print(i, end=" ")