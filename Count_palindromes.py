n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    s=0
    q=i
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==i:
        c=c+1
print(c)