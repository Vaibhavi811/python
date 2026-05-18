# sum and avearge of your own registration no
reg_no= input("Enter your reg no:")
sum=0
count=0

for i in reg_no:
    if(i.isdigit()):
        sum=sum+int(i)
        count+=1
print("sum of the digits in reg no:", sum)
average= sum//count
print("avg of the digits in reg no:", average)


