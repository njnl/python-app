year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("THE YEAR IS A LEAP YEAR!)
else:
    print("The year isn't a leap year!)
