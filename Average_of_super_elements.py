n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    x=a.count(a[i])
    if x==a[i]:
        if a[i] not in b:
            b.append(a[i])
if len(b)!=0:
    av=sum(b)/len(b)
    print(format(av,".2f"))
else:
    print('-1')