num=int(input("enter a number"))
rev=0
temp=num
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if num==rev:
    print(num,"is an palindrome")
else:
    print(num,"is not palindrome")
    




