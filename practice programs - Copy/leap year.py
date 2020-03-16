year=int(input("enter numbers"))
if year%4==0 or year%400==0:
    print(year,"leap year")
else:    
    print(year,"not leap year")
