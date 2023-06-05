def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
for i in range(n,2*n+1):
    if fun(i)==1:
        p=i
        break
for i in range(n,1,-1):
    if fun(i)==1:
        q=i
        break 
if abs(p-n)==abs(q-n):
    print(abs(p-n))
elif abs(p-n)>abs(q-n):
    print(abs(q-n))
else:
    print(abs(p-n))