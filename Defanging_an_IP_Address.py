s=input()
b=[]
for i in s:
    if i=='.':
        b.append('[.]')
    else:
        b.append(i)
for i in b:
    print(i,end="")