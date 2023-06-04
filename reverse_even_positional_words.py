s=input()
s=s.split(' ')
b=[]
for i in range(0,len(s)):
    if i%2==0:
        x=s[i]
        x=x[::-1]
        b.append(x)
    else:
        b.append(s[i])
print(*b)