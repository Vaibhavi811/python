# 2. Write a Program to calculate arithmetic operation on two number using user defined  
# function  
def arithmetic(a=5,b=11,c="+"):
    if(c=="+"):
        return a + b
    elif(c=="-"):
        return a - b
    elif(c=="*"):
        return a * b
    elif(c=="/"):
        return a / b
    elif(c=="**"):
        return a ** b
    elif(c=="%"):
        return a % b
    elif(c=="//"):
        return a // b
    else:
        return -1
a= int(input("Enter the value:"))
b= int(input("Enter the value:"))
c= input("enter the operator:")

x= arithmetic(a,b,c)
print(x)
