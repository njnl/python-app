year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
   
    print(year, "is Leap Year!)

else:
    print(year, "isn't a leap year!)
          
          
print(f"You enterded, year is {year} and taht is not leap year")