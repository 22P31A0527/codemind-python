n=int(input())
arr=list(map(int,input().split()))
x=0
for i in arr:
    if i%2==0:
        x=i
print(x)    