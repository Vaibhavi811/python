# Check if a tuple is a palindrome
t=(2,3,5,3,2)

rev_t= t[::-1]
if(t== rev_t):
    print("Tuple is a palindrome")
else:
    print("NOt a palindrome")
