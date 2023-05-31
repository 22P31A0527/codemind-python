n=int(input())
a=list(map(int,input().split()))
b=[]
s=[]
for i in range(0,n):
    if a[i] not in b:
        b.append(a[i])
        x=a.count(a[i])
        s.append(x)
m=len(b)
for i in range(0,m):
    print(b[i],s[i],end=" ")
    