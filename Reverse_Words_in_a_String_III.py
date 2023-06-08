s=input()
s=s.split(' ')
for i in range(0,len(s)):
    x=s[i]
    s[i]=x[::-1]
for i in s:
    print(i,end=" ")