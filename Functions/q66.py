#  Write a Program to find small number between two numbers using Lambda function
num1= int(input("Enter any num:"))
num2=int( input("Enter any num:"))
result= lambda num1,num2: num1>num2

if(result(num1,num2)):
    print(num2, "is smaller")
else:
    print(num1, "is smaller")