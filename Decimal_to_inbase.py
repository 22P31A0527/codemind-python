n=int(input())
m=int(input())
b=[]
while n!=0:
    if n%m==0:
        b.append(0)
    else:
        b.append(n%m)
    n=n//m
ma=0
for i in range(0,len(b)):
    if b[i]==0:
        c=0
        for j in range(i,len(b)):
            if b[j]==b[i]:
                c+=1
            else:
                break
        if c>ma:
            ma=c
if ma!=0:
    print(ma)
else:
    print('-1')