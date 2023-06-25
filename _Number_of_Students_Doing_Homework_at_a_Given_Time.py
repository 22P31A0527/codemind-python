n=int(input())
s=list(map(int,input().split()))
m=int(input())
e=list(map(int,input().split()))
q=int(input())
c=0
for i in range(0,n):
    if q>=s[i] and q<=e[i]:
        c+=1
print(c)