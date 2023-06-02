n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    x=a.count(i)
    if i not in b:
        b.append(i)
        c=c+(x//2)
print(c)