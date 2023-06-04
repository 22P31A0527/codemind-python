s=input()
a='aeiouAEIOU'
b=[]
for i in range(0,len(s)):
    if s[i] in a:
        if s[i] not in b:
            b.append(s[i])
print(*b)