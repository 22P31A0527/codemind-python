n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    if a[i]==1:
        s=s+2**(n-i-1)
print(s)