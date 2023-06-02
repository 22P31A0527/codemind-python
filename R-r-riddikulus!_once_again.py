n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(k,n):
    b.append(a[i])
for i in range(0,k):
    b.append(a[i])
print(*b)