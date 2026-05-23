# Write a python program to find factorial of a number using Recursion.
def fact(n=5):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)
    
result= fact(4)
print(result)
