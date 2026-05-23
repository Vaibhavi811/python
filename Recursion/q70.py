# WAP to calculate power of a number using recursion
def fun(num=5, n=3):
    if(n==0):
        return 1
    else:
        return num * fun(num, n-1)
    
result= fun(2,3)
print(result)