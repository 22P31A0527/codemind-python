n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c==i and i not in b:
        b.append(i)
if b!=[]:
    for i in b:
        print(i,end=" ")
else:
    print('-1')