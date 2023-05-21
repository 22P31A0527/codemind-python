import math
q=int(input())
n=q
s=0
j=str(q)
i=len(j)
while n!=0:
    r=n%10
    s=s+pow(r,i)
    i-=1
    n=n//10
if s==q:
    print(True)
else:
    print(False)