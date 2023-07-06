s=input()
s=s.lower()
l1=[]
l2=''
for i in range(0,len(s)):
    if s.count(s[i])==1 and s[i]!=' ':
        x=ord(s[i])
        if x not in l1:
            l1.append(x)
l1.sort()
for i in range(0,len(l1)):
    l2=l2+chr(l1[i])
print(l2)