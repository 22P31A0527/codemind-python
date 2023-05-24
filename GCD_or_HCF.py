n,m=map(int,input().split())
for i in range(1,n and m):
    if n%i==0 and m%i==0:
        g=i
print(g)