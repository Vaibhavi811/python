# 1. Write a Program to write user defined function to swap two number and display number  
# before swapping and after swapping 
def swap(a=2,b=5):
    b=a+b
    a=b-a
    b=b-a
    print("after swapping:",a,b)

a=2
b=7
print("Before swapping:",a,b)
swap(a,b)
