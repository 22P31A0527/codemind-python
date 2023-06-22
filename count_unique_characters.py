s=input()
c=0
s=s.lower()
for i in range(0,len(s)):
    if s.count(s[i])==1 and s[i]!=' ':
        c+=1
print(c)