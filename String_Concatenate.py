s1=input()
s2=input()
s=s1+s2
l=[]
for i in range(0,len(s)):
    l.append(ord(s[i]))
l.sort()
p=''
for i in range(0,len(l)):
    p=p+chr(l[i])
print(p)