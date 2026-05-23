# Write a Program to print Fibonacci series up to n terms using recursion
def fib(n=5):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n= int(input("Enter the value of range:"))
for i in range(n):
    print(fib(i),"",end="")