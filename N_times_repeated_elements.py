n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=[]
x=0
for i in a:
    if a.count(i)==m:
        if i not in b:
            b.append(i)
            x=1
if x==1:
    for i in range(0,len(b)):
        print(b[i],end=" ")
else:
    print('-1')