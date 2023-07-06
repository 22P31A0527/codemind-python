n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in range(0,n):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
i=j=0
s=[]
while i<len(e) and j<len(o):
    s.append(e[i])
    s.append(o[j])
    i+=1
    j+=1
while i<len(e):
    s.append(e[i])
    i+=1
while j<len(o):
    s.append(o[j])
    j+=1
if len(s)%2!=0:
    s.append('0')
print(*s)