n=int(input())
arr=list(map(int,input().split()))
se=int(input())
c=0
for i in arr:
    if i==se:
        c+=1
print(c)