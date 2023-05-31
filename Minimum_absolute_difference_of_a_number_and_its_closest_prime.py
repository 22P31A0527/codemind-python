def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:return 0
    return 1
n=int(input())
for i in range(n,n*2+1):
    if fun(i)==1:
        x=i
        break
for i in range(n,1,-1):
    if fun(i)==1:
        y=i
        break
if abs(n-x)==abs(n-y):
    print(abs(n-x))
elif abs(n-x)<abs(n-y):
    print(abs(n-x))
else:
    print(abs(n-y))