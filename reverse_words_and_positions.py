s=input()
s=s.split(' ')
s=s[::-1]
b=[]
for i in s:
    i=i[::-1]
    b.append(i)
print(*b)