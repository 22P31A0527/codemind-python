n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]>=m:
        c+=1
print(c)
    