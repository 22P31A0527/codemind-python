n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2==0:
        s=1
    else:
        s=0
        break
if s==1:
    print(True)
else:
    print(False)