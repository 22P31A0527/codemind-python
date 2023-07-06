n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(0,n):
    if a[i]>0:
        x=a[i]
    else:
        x=-a[i]
    s=str(x)
    if len(s)==m:
        l.append(s)
print(len(l))