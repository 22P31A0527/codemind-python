s=input()
s1=''
c=0
for i in range(0,len(s)):
    if s[i]=='9':
        s1=s1+s[i]
    else:
        if c==0:
            s1=s1+'9'
            c+=1
        else:
            s1=s1+'6'
print(s1)