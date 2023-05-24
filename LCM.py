n,m=map(int,input().split())
for i in range(1,m+1):
    if i*n%m==0:
        print(i*n)
        break