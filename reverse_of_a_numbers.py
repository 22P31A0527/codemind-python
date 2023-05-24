k=int(input())
s=0
while k!=0:
    r=k%10
    s=s*10+r
    k=k//10
print(s)