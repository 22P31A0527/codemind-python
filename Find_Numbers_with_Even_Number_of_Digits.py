n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    x=len(str(i))
    if x%2==0:
        c+=1
print(c)