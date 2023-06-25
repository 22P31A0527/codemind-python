n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(0,n):
    if a[i]==1:
        c=0
        for j in range(i,n):
            if a[j]==a[i]:
                c+=1
            else:
                break
        if c>m:
            m=c
print(m)