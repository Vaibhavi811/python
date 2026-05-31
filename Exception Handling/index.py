# Program to illustrate handling of Index Error Exception
try:
    a=[10,20,30,40]
    index_no= int(input("Enter index no:"))
    print("Element:",a[index_no])

except IndexError:
    print("Error: Index out of range.")