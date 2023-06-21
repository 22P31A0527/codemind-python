s=input()
l=[]
v='aeiouAEIOU'
for i in range(0,len(s)):
    if s[i] in v:
        l.append(s[i])
j=len(l)-1
s1=''
for i in range(0,len(s)):
    if s[i] in v:
        s1=s1+l[j]
        j-=1
    else:
        s1=s1+s[i]
print(s1)
    