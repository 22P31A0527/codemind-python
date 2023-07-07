s1=input().lower()
s2=input().lower()
s1=s1.split(' ')
s2=s2.split(' ')
l=[]
for i in range(0,len(s2)):
    if s2[i] in s1:
        l.append(s2[i])
print(*l)