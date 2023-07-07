s1=input().lower()
s2=input().lower()
s2=s2.split(' ')
s=''
for i in range(0,len(s2)):
    x=s2[i]
    for i in range(0,len(x)):
        if x[i] in s1:
            if x[i] not in s:
                s=s+x[i]
print(len(s))