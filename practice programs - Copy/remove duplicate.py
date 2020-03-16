s=input("enter a charachers")
r=""
for ch in s:
    if ch not in r:
        r=r+ch
print(r)    



           (OR)
s=input("enter characters")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
output="".join(l)
print(output)
        
