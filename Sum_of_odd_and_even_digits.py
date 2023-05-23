n=int(input())
a=list(map(int,input().split()))
s=p=0
for i in range(n):
    if i%2==0:
        s=s+a[i]
    else:
        p=p+a[i]
if abs(s-p)==0:
    print('YES')
else:
    print('NO')