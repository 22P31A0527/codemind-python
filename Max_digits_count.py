def fun(n):
    c=0
    while n!=0:
        r=n%10
        c=c+1
        n=n//10
    return c
n=int(input())
a=list(map(int,input().split()))
m=0
for i in a:
    x=fun(i)
    if x>m:
        m=x
ma=0
for i in a:
    y=fun(i)
    if y==m:
        ma=ma+1
print(ma)