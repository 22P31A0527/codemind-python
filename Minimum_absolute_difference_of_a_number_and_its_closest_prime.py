def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:return 0
    return 1
n=int(input())
for i in range(n,2*n+1):
    if fun(i)==1:
        a=i
        break
for i in range(n,0,-1):
    if fun(i)==1:
        b=i
        break
if abs(n-a)==abs(n-b):
    print(abs(n-a))
elif abs(n-a)<abs(n-b):
    print(abs(n-a))
else:
    print(abs(n-b))