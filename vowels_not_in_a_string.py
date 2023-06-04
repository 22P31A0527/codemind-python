s=input()
a='aeiou'
b=[]
for i in range(0,len(s)):
    if s[i] in a:
        if s[i] not in b:
            b.append(s[i])
if len(a)==len(b):
    print('0')
else:
    for i in a:
        if i not in b:
            print(i,end=" ")