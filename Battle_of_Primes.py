def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
for i in range(1,a*b):
    s=a+b+i
    if fun(s)==1:
        print(i)
        break