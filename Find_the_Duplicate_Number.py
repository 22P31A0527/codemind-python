n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    if a.count(a[i])>1:
        print(a[i])
        break