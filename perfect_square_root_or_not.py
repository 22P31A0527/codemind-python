import math
n=int(input())
k=int(math.sqrt(n))
if n==k*k:
    print(True)
else:
    print(False)