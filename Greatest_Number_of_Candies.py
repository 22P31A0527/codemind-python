n=int(input())
a=list(map(int,input().split()))
excan=int(input())
l=[]
for i in range(0,n):
    x=a[i]
    a[i]=a[i]+excan
    if max(a)==a[i]:
        l.append(True)
    else:
        l.append(False)
    a[i]=x
print(*l)