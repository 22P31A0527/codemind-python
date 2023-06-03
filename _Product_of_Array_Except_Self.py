n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    p=1
    for j in range(0,n):
        if i!=j:
            p=p*a[j]
    b.append(p)
print(*b)