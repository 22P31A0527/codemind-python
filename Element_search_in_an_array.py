n=int(input())
ar=list(map(int,input().split()))
k=int(input())
s=0
for i in ar:
    if i==k:
        s=1
        break
if s==1:
     print(True)
else:
    print(False)