s=input()
l='aeiou'
u='AEIOU'
a=[]
b=[]
for i in range(0,len(s)):
    if s[i] in l:
        if s[i] not in a:
            a.append(s[i])
    elif s[i] in u:
        if s[i] not in b:
            b.append(s[i])
if len(l)==len(a) or len(u)==len(b):
    print(True)
else:
    print(False)