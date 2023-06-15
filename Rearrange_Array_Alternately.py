t=int(input())
for k in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    i=0
    j=n-1
    while i<=j:
        b.append(a[j])
        j-=1
        if a[i] not in b:
            b.append(a[i])
            i+=1
    print(*b)