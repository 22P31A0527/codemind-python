def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
def fun1(n):
    q=n
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==n:
        return 1
    return 0
n=int(input())
i=n+1
while 1:
    if fun(i)==1 and fun1(i)==1:
        print(i)
        break
    i+=1