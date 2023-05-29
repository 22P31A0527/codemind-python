a=int(input())
b=int(input())
for i in range(a,b):
    q=i
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==i:
        print(i,end=" ")