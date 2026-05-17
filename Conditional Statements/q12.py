#  wap to create a simple calculator using if-elif and perform operations(+,-,*,/)
a= int(input("enter a:"));
b= int(input("enter b:"));
c=str(input("Enter any operator:"));

if(c=='*'):
    print(a*b);
elif(c=='/'):
    if(b!=0):
        print(a/b);
    else:
        print("Invaild, b cannot be 0");
elif(c=='+'):
    print(a+b);
elif(c=='-'):
    print(a-b);
else:
    print("Invalid operator");