def fun(n):
    q=n
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==n:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,2*n+1):
    if fun(i)==1:
        a=i
        break
for i in range(n-1,0,-1):
    if fun(i)==1:
        b=i
        break
if abs(n-a)==abs(n-b):
    print(b,a)
elif abs(n-a)<abs(n-b):
    print(a)
else:
    print(b)