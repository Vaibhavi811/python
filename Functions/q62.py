# Write a function that takes three numbers as parameters, and returns the median value
def mediann(a=2,b=5,c=8):
    list1= [a,b,c]
    list1.sort()
    return list1[1]

a=100
b=26
c=46
x= mediann(a,b,c)
print(x)