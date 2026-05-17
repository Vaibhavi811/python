# wap to swap two nos and display them before and after swapping
a=int(input("enter a:"));
b=int(input("enter b:"));

print("Before swapping", a,b);

a=a+b;
b=a-b;
a=a-b;
print("After swapping", a,b);