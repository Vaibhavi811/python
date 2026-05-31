# Program to illustrate handling of Type Exception
try:
    a= int(input("Enter any no:"))
    b=input("Enter any string:")
    result= a + b
    print("Result:", result)

except TypeError:
    print("Error: Cannot add integer and string together.")