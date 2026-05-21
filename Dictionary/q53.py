# 5. Two words are anagrams if they contain all of the same letters, but in a different order.  
# For example, “evil” and “live” are anagrams because each contains one ‘e’, one ‘I’, one  
# ‘l’, and one ‘v’. Create a program that reads two strings from the user, determines  
# whether or not they are anagrams, and reports the result.
str1= input("enter the string1:")
str2= input("enter the string2:")

str1=str1.replace(" ","").lower()
str2= str2.replace(" ", "").lower()

if(sorted(str1)==sorted(str2)):
    print("They are anagrams")
else:
    print("Not anagrams")