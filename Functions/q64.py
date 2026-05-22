# Write a Program to filter even values from list using lambda function
list1= [1,2,4,5,9,8,65,28]
list2= list(filter(lambda x:x%2==0,list1))

print(list2)

def even(list3):
    list4= []
    for i in list3:
        if(i%2==0):
            list4.append(i)
    print(list4)

even(list1)

