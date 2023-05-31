def fun(n):
    q=n
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==n:
        return 1
    return 0
n=int(input())
for i in range(n+1,2*n+1):
    if fun(i)==1:
        x=i
        break
for i in range(n-1,0,-1):
    if fun(i)==1:
        y=i
        break
if abs(n-x)==abs(n-y):
    print(y,x)
elif abs(n-x)<abs(n-y):
    print(x)
else:
    print(y)
        