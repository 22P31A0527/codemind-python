t=int(input())
for i in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    s1=n*(n+1)/2
    s2=0
    for i in range(0,n-1):
        s2=s2+a[i]
    print(int(s1-s2))