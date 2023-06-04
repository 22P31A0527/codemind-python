s=input()
s=s.split(' ')
b=[]
for i in range(0,len(s)):
    x=s[i]
    b.append(x[::-1])
print(*b)