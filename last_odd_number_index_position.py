n=int(input())
f=list(map(int,input().split()))
for i in range(len(f)):
    if f[i]%2!=0:
        r=i
print(r)