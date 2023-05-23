n=int(input())
c=0
a=list(map(int,input().split()))
m=sum(a)//len(a)
for i in range(len(a)):
    if m==a[i]:
        c+=1
        break
if c==1:
    print(True)
else:
    print(False)