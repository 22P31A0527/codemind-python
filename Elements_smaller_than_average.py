n=int(input())
k=0
a=list(map(int,input().split()))
c=sum(a)//len(a)
for i in range(len(a)):
    if a[i]<=c:
        k+=1
print(k)