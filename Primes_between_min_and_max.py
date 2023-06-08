def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
m1=a.index(max(a))
m2=a.index(min(a))
c=0
if m1<m2:
    for i in range(m1,m2):
        if fun(a[i])==1:
            c+=1
else:
    for i in range(m2,m1+1):
        if fun(a[i])==1:
            c+=1
print(c)