n=int(input())
a=list(map(int,input().split()))
m1=0
m2=0
m3=0
for i in a:
    if i>m1:
        m1=i
for i in a:
    if i>m2 and i<m1:
        m2=i
for i in a:
    if i>m3 and i<m2 and i<m1:
        m3=i
if m3>0:
    print(m3)
else:
    print(m1)