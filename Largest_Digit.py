k=int(input())
s=0
while k!=0:
    r=k%10
    if r>s:
        s=r
    k=k//10
print(s)