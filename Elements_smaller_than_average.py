n=int(input())
c=0
a=list(map(int,input().split()))
m=sum(a)//len(a)
for i in range(len(a)):
    if a[i]<=m:
        c+=1
print(c)