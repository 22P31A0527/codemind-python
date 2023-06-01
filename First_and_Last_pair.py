n=int(input())
a=list(map(int,input().split()))
b=[]
m=n//2+1
i=0
j=n-1
while i<=m and j>=m:
    b.append(a[i])   
    i+=1
    b.append(a[j])
    j-=1
if n%2!=0:
    b.append(a[i])
    print(*b,'0')
else:
    b.append(a[i])
    b.append(a[j])
    print(*b)