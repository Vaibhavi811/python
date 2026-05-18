# wap to check whether a string is palindrome or not

text= input("Enter any string:")
text= text.upper()
rev_text= text[::-1]

if(text == rev_text):
    print("String is palindrome.")
else:
    print("Not a palindrome.")