n=int(input())
s=x=0
a=list(map(int,input().split()))

for i in range(n-1,-1,-1):
    s=s+a[i]*(2**x)
    x=x+1
print(s)
    