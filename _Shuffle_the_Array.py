n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=[]
x=[]
y=[]
for i in range(0,m):
    x.append(a[i])
for i in range(m,n):
    y.append(a[i])
for i in range(0,len(x)):
    b.append(x[i])
    b.append(y[i])
print(*b)