s=input()
s=s.split(' ')
for i in range(0,len(s)):
    a='aeiouAEIOU'
    x=s[i]
    c=0
    for i in range(0,len(x)):
        if x[i] in a:
            c=c+1
    print(c,end=" ")