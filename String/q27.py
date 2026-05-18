# wap to create,concatenate, and print a string and accessing sub string from a given string.
string= str(input("Enter your name:"))

ans= str(input("Do you want to concatenate two strings(Y/N):"))
if(ans=="Y" or ans=="y"):
    string2= str(input("Enter the string:"))
    print(string+ " "+ string2)
else:
    print("Thankyou.")
ans1= str(input("Do you want to access sub string(Y/N):"))
if(ans1=="Y" or ans1=="y"):
    start= int(input("Enter the start:"))
    end= int(input("Enter the end:"))
    print(string[start:end])
else:
    print("Thankyou.")