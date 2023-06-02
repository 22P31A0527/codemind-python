n=int(input())
m=int(input())
s=0
for i in range(1,n+1):
    a=list(map(int,input().split()))
    for i in a:
        s=s+i
print(s)