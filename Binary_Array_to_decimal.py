n=int(input())
a=list(map(int,input().split()))
x=0
s=0
for i in range(n-1,-1,-1):
    s=s+a[i]*(2**x)
    x=x+1
print(s)