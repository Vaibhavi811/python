# wap to print a list in ascending and descending order
list=[]
while(True):
    num= int(input("enter a no:"))
    if(num==0):
        break
    else:
        list.append(num)
list.sort()
print("Ascending order:", list)
list.reverse()
print("Descending order:", list)