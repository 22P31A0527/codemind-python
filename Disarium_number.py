n=int(input())
k=n
c=s=0
while n!=0:
    c+=1
    n=n//10
n=k
while n>0:
    r=n%10
    s=s+r**c
    n=n//10
    c=c-1
if s==k:
    print(True)
else:
    print(False)