num=int(input("enter number"))
fact=1
if num<0:
    print("factorial desnot support negitive values")
elif num==0:
    print("fact o is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)    
    
    
