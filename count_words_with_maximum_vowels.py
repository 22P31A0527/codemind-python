s=input()
s=s.split()
v='aeiou'
l=[]
for i in range(0,len(s)):
    x=s[i]
    c=0
    for i in range(0,len(x)):
        if x[i] in v:
            c+=1
    l.append(c)
m=max(l)
print(l.count(m))