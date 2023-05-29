def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n1=int(input())
n2=int(input())
t=n1+n2
for i in range(1,t):
    if fun(t+i)==1:
        print(i)
        break