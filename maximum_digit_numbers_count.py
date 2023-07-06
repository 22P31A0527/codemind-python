n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n):
    l.append(len(str(a[i])))
m=max(l)
l1=[]
for i in range(0,n):
    s=str(a[i])
    if len(s)==m:
        l1.append(s)
print(*l1)