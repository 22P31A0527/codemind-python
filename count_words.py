s=input()
v='aeiouAEIOU'
s=s.split(' ')
c=0
for i in range(0,len(s)):
    x=s[i]
    if x[0] in v and x[len(x)-1] not in  v:
        c=c+1
print(c)   