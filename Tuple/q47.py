# Find 2nd largest element in a tuple
t=(2,2,54,54,66,21,89,94,94)

list1= list(set(t))
print(list1)

list1.sort()
print(list1)

last_element= list1[-2]
print(last_element)