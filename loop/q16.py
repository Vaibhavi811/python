# wap to find the sum of digits of a number
n= int(input("enter the numbers:"));

sum=0;
while(n!=0):
    rem=n%10;
    sum=sum+rem;
    n=n//10;
print("sum of number:",sum)
