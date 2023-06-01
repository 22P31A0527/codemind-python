n=int(input())
if n>0:
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    print(s)
else:
    s=0
    n=-(n)
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    print(-s)