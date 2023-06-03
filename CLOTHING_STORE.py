n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if i not in b:
        b.append(i)
        c=c+(a.count(i)//2)
print(c)