def fun(n):
    s=0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
x=int(input())
while 1:
    x=x+fun(x)
    if x==fun(x):
        print(x)
        break