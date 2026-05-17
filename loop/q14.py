# wap to find the factorial of a number
n= int(input("Enter the value of n:"));

fact=1;
i=1;
while(i<=n):
    fact=fact*i;
    i=i+1;
print("Factorial of n is:", fact);

factf=1;
for i in range(1,n+1):
    factf=factf*i;
print("Factorial of n is:", factf);
