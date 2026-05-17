# check whether a given no is armstrong or not
num= int(input("Enter a number:"))
count=0
sum=0
n= num
while(num!=0):
    num=num//10;
    count+=1

num=n
while(n!=0):
    rem=n%10
    sum=rem**count + sum
    n= n//10

if(sum==num):
    print("NO is Armstrong");
else:
    print("Not a armstrong")

