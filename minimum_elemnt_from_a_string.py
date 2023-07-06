s=input()
s=s.split(' ')
s=s[len(s)-1]
l=[]
for i in range(0,len(s)):
    l.append(ord(s[i]))
m=min(l)
m=chr(m)
if m.lower() in s:
    print(m.lower())
else:
    print(m)