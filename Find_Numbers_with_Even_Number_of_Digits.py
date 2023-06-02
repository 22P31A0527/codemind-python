def fun(n):
    x=0
    while n!=0:
        r=n%10
        x=x+1
        n=n//10
    if x%2==0: return 1
    else:return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    p=fun(i)
    if p==1:
        c+=1
print(c)