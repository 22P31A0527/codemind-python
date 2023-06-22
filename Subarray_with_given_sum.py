t=int(input())
for k in range(1,t+1):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(0,n):
        s=0
        for j in range(i,n):
            s=s+a[j]
            if s==m:
                break
        if s==m:
            print(i+1,j+1)
            break
    else:
        print('-1')