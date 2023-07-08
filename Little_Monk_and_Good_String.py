s=input()
d=0
v='aeiou'
for i in range(0,len(s)):
    c=''
    if s[i] in v:
        for j in range(i,len(s)):
            if s[j] in v:
                c=c+s[j]
            else:
                break
        if len(c)>d:
            d=len(c)
print(d)