import math
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    m=int(math.sqrt(i))
    if m*m==i:
        s=s+i
print(s)