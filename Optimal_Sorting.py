n=int(input())
for i in range(1,n+1):
    m=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if a==b:
        print('0')
    else:
        x=max(b)-min(b)
        print(x)