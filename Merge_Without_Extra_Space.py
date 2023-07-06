t=int(input())
for i in range(1,t+1):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=a+b
    c.sort()
    print(*c)