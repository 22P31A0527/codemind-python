n=int(input())
a=list(map(int,input().split()))
x=a.count(0)
y=a.count(1)
b=[]
for i in range(0,x):
    b.append(0)
for i in range(0,y):
    b.append(1)
print(*b)