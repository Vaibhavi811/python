# 4. Write a Program that determines and displays the number of unique characters in a string  
# entered by the user. For example, “Hello, World!” has 10 unique characters while “zzz”  
# has only one unique character. Use a dictionary to solve this problem.  
str= input("enter the string:")
dic={}

for ch in str:
    dic[ch]=1
print(len(dic))