n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    if i==a.count(i):
        if i not in b:
            b.append(i)
            s=s+i
if s>0:
    t=s/len(b)
    print(format(t,".2f"))
else:
    print('-1')