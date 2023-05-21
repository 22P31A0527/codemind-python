def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n1=int(input())
n2=int(input())
n12=n1+n2
for i in range(1,n12):
    if fun(n12+i)==1:
        print(i)
        break
