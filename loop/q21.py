# Wap to check whether a no is palindrome or not. 
num=int(input("Enter any no:"))
sum= 0
n= num
while(num!=0):
    rem=num%10
    sum= sum*10 + rem
    num=num//10

if(n==sum):
    print("Number is palindrome")

else:
    print("Number is not a palindrome")