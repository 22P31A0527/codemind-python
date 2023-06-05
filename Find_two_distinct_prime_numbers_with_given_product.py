def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
for i in range(2,n//2+1):
    if n%i==0:
        if fun(i)==1:
            n1=i
            n2=n//i
            if fun(n2)==1:
                print(n1,n2)
                break
else:
    print('-1')