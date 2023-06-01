n=int(input())
a=list(map(int,input().split()))
c=0
m=0
for i in a:
    x=a.count(i)
    if x>m: 
        m=x
        y=i
print(y)