s=input()
a='1234567890'
c=0
for i in s:
    if i in a:
        c=c+int(i)
print(c)