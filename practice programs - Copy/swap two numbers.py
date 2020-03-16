a=int(input("enter number"))
b=int(input("enyter number"))
temp=a
a=b
b=temp
print(a,b)

#with out using third variable

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)
