s=input()
a='aeiouAEIOU'
c=0
for i in range(0,len(s)):
    if s[i] in a:
        c+=1
print(c)