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
    if fun(s)==1:
        return 1
    return 0
n=int(input())
if fun(n)==1 and fun1(n)==1:
    print('circular prime')
elif fun(n)==1 and fun1(n)==0:
    print('prime but not a circular prime')
else:
    print('not prime')