year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("THIS IS JUST A LEAP YEAR!)
elif year%2==0:
    print("Bu satır lokal feature branch inde eklendi")
:wqelse:
    print("The year isn't a leap year!)
