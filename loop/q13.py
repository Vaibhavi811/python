# wap to find sum of first n natural numbers
n= int(input("Enter the value of n:"));

i=1;
sum=0;
while(i<=n):
    sum=sum+i;
    i=i+1;
print(" sum of first n natural numbers",sum);

sumf=0;
for i in range(1,n+1):
    sumf=sumf+i;
print(" sum of first n natural numbers",sumf);