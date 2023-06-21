s=input()
m=''
for i in range(0,len(s)):
    b=''
    for j in range(i,len(s)):
        if len(b)==0:
            b=b+s[j]
        elif s[j]==b[len(b)-1]:
            b=b+s[j]
        else:
            break
    if len(b)>len(m):
        m=b
print(len(m))