# wap to count the number of digits in a number
n= int(input("Enter the number:"));

count=0;
while(n!=0):
    n=n//10;
    count=count+1;
print("number of digits in a number:",count)

no= str(input("enter the number:" ))
countf=0;
for i in range(len(no)):
    countf=countf+1;
print("number of digits in a number:",countf)