# wap to check whether an entered year is leap or not.
year=int(input("year"));

if(year%4==0) and (year%400==0) or (year%100==0):
    print("its a leap year");

else:
    print("its not a leap year");
