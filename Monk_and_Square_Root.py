t=int(input())
for k in range(1,t+1):
    n,m=map(int,input().split())
    for i in range(0,m):
        x=i*i
        if x%m==n:
            print(i)
            break
    else:
        print('-1')