# wap to count all letters, digits, and special symbols from a given string.
string= input("Enter a string:")
letters= 0
digits= 0
special_symbols= 0

for i in string:
    if(i.isalpha()):
        letters+=1
    elif(i.isdigit()):
        digits+=1
    else:
        special_symbols+=1
print("Letters in a string:", letters)
print("Digits in a string:", digits)
print("Special symbols in a string:", special_symbols)
