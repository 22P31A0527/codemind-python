def fun(n):
    q=n
    while q!=0:
        r=q%10
        if r==0:
            return 0
        elif n%r!=0:
            return 0
        q=q//10
    return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if fun(i)==1:
        print(i,end=" ")