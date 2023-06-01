n=int(input())
a=list(map(int,input().split()))
for i in a:
    q=i
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    print(s,end=" ")