def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
if fun(n)==1:
    print('prime')
else:
    print('not a prime')