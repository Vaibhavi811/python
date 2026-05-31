# Program to illustrate handling of Divide by Zero Exception
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    result= a/b
    print("Divison of a by b:", result)

except ZeroDivisionError:
    print("Error: Divison by 0 is not allowed.")