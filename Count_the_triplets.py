t=int(input())
for k in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            x=a[i]+a[j]
            if x in a:
                c+=1
    if c!=0:
        print(c)
    else:
        print('-1')