s=input()
s=s.lower()
b=[]
for i in range(0,len(s)):
    if s[i]!=' ':
        if s[i] not in b:
            b.append(s[i])
print(len(b))