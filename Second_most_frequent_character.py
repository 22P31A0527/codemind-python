s=input()
m1=0
for i in s:
    if s.count(i)>m1:
        m1=s.count(i)
        p1=i
m2=0
p2=-1
for i in s:
    if s.count(i)>m2 and s.count(i)<m1:
        m2=s.count(i)
        p2=i
print(p2)