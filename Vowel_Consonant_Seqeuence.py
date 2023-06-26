s=input()
v='aeiou'
s1=''
for i in range(0,len(s)):
    if len(s1)==0:
        if s[i] in v:
            s1=s1+'V'
        else:
            s1=s1+'C'
    elif s[i] in v:
        if s1[len(s1)-1]!='V':
            s1=s1+'V'
    else:
        if s1[len(s1)-1]!='C':
            s1=s1+'C'
print(s1)