s=input()
m=[]
for i in range(0,len(s)):
    b=[]
    for j in range(i,len(s)):
        x=s[j].lower()
        y=s[j].upper()
        if x not in b and y not in b:
            b.append(s[j])
        else:
            break
    if len(b)>len(m):
        m=b
if len(m)>=3:
    for i in range(0,len(m)):
        print(m[i],end="")
else:
    print('-1')