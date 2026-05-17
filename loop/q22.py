# construct a pattern
i=1
while(i<=5):
    j=1
    while(j<=i):
        print("*", end="")
        j=j+1
    print("")
    i=i+1
i=5
while(i>=1):
    j=i
    while(j>0):
        print("*",end="")
        j=j-1
    print("")
    i=i-1