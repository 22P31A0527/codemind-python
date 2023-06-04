n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if a.count(i)>c:
        c=a.count(i)
        x=i
    elif a.count(i)==c:
        c=a.count(i)
        if i<x:
            x=i
print(x)