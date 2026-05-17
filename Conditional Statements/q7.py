# wap to find largest among 3 no
a=int(input("a:"));
b=int(input("b:"));
c=int(input("c:"));

if(a>b):
    if(a>c):
        print("a is largest");
    else:
        print("c is largest");
else:
    if(b>c):
        print("b is largest");
    else:
        print("c is largest");