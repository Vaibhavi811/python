# Program to illustrate handling of ValueError Exception
try:
    a=int(input("enter any no:"))
    print("Entered Number:",a)

except ValueError:
    print("Error: Invalid input. Please enter only number.")