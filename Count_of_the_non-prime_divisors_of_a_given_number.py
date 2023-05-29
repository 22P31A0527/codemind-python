def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 1
    return 0
n=int(input())
c=1  ##already 1 is counted
for i in range(2,n+1):
    if n%i==0:
        if fun(i)==1:
            c+=1
print(c)