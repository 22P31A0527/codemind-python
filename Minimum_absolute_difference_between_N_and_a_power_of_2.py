n=int(input())
for i in range(0,n):
    x=2**i
    if x>=n:
        break
    y=x
if abs(n-x)<abs(n-y):
    print(abs(n-x))
else:
    print(abs(n-y))