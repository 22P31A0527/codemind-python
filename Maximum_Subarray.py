n=int(input())
a=list(map(int,input().split()))
m=a[0]
for i in range(0,n):
    s=0
    for j in range(i,n):
        s=s+a[j]
        if s>m:
            m=s
print(m)