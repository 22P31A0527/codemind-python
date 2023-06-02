s=input()
x='0123456789'
c=0
for i in range(0,len(s)):
    if s[i] in x:
        c=c+int(s[i])
print(c)