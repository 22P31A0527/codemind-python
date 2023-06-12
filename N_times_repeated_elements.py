n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=[]
for i in range(0,n):
    if a.count(a[i])==m:
        if a[i] not in b:
            b.append(a[i])
if len(b)>0:
    print(*b)
else:
    print('-1')