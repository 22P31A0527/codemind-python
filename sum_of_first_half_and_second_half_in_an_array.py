n=int(input())
a=list(map(int,input().split()))
m=n//2
p=0
q=0
for i in range(0,m):
    p=p+a[i]
for i in range(m,n):
    q=q+a[i]
print(p)
print(q)