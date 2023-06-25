n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
m=int(input())
s=0
for i in range(0,n):
    if a[i]<=m:
        s=s+1
    else:
        s=s+2
print(s)