k=int(input())
n=k*k
s=b=0
while k!=0:
    r=k%10
    s=s*10+r
    k=k//10
f=s*s
while f>0:
    j=f%10
    b=b*10+j
    f=f//10
if b==n:
    print(True)
else:
    print(False)