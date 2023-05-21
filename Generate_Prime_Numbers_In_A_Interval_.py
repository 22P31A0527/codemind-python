def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
for i in range(a+1,b):
    x=fun(i)
    if x==1:
        print(i)