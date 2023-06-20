s=input()
a='aeiou'
ss=''
m=''
for i in range(0,len(s)):
    if s[i] in a:
        ss=''
        for j in range(i,len(s)):
            if s[j] in a:
                ss=ss+s[j]
            else:
                break
        if len(ss)>len(m):
            m=ss
print(len(m))