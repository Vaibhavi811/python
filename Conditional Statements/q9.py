# Write a program in python to print a grade according to a student's mark with multiple if
# statements
mark=int(input("Enter the marks:"));
if(mark>=80):
    print("excellent");
elif(mark>=65) and (mark<80):
    print("Good");
elif(mark>=50) and(mark<65):
    print("Pass");
elif(mark<50):
    print("fail");
    

    