s=input()
m=''
for i in range(0,len(s)):
    t='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'
    for j in range(i,len(s)):
        t=t+s[j]
        if t==t[::-1]:
            if len(t)>len(m):
                m=t
print(m)