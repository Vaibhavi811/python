# Write a program that reads values from the user until a blank line is entered. Display the  
# total of all of the values entered by the user (or 0.0 if the first value entered is a blank  
# line). Complete this task using recursion. Your program may not use any loops.

def sum():
    n=input("Enter any value:")
    if(n==""):
        return 0.0
    else:
        return float(n) + sum()
    
result= sum()
print(result)