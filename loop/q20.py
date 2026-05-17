# Wap to check whether the entered no is prime or not
num= int(input("Enter a num:"))
ans=1

i=2
while(i<=num//2):
    if(num%i==0):
        ans=0
        break
    i=i+1;

if(ans==1):
    print("Num is prime")