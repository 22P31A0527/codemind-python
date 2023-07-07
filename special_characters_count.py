##65 90   97 122   48 57
s=input()
c=d=0
for i in range(0,len(s)):
    x=ord(s[i])
    if s[i]!=' ':
        if x>=65 and x<=90:
            c+=1
        elif x>=97 and x<=122:
            c+=1
        elif x>=48 and x<=57:
            c+=1
        else:
            d+=1
print(d)