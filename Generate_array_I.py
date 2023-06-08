n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    x=a[i]
    y=a[i+1]
    for i in range(1,y+1):
        b.append(x)
print(*b)