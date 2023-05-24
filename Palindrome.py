n=int(input())
k=n
s=0
while k!=0:
    r=k%10
    s=s*10+r
    k=k//10
if s==n:
    print(True)
else:
    print(False)