n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    if a.count(i)==1:
        s=1
        b.append(i)
if s==1:
    print(max(b))
else:
    print('-1')