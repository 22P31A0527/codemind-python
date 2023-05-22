def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
for i in range(2,n):
    if n%i==0 and fun(i)==1:
        if fun(n//i)==1 and i*(n/i)==n:
            print(i,n//i)
            break
else:
    print('-1')