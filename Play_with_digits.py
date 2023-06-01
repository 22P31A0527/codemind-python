n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    q=i
    while q!=0:
        r=q%10
        s=s+r
        q=q//10
print(s)