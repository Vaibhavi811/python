# WAP to Count Frequency of Elements in a List
list1= [1,2,2,3,4,1,2,3]
dict= {}

for items in list1:
    if items in dict:
        dict[items]+=1
    else:
        dict[items]=1
    
print("Frequency:", dict)