import math
n=int(input())
for i in range(1,n+1):
    k=int(input())
    s=int(math.sqrt(k))
    if k==s*s:
        print(True)
    else:
        print(False)