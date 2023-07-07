n=int(input())
a=list(map(int,input().split()))
a[n-1]=a[n-1]+1
if a[n-1]<10:
    print(*a)
else:
    x=0
    for i in range(n-1,-1,-1):
        a[i]=a[i]+x
        x=a[i]//10
        if a[i]>9:
            a[i]=a[i]%10
    if x==0:
        print(*a)
    else:
        print(x,*a)