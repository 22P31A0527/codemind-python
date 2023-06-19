n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    s=0
    for j in range(i,n):
        s+=a[j]
        if s==m:
            c+=1
            break
print(c)