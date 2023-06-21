t=int(input())
for k in range(1,t+1):
    s=input()
    c=0
    b=''
    for i in range(0,len(s)):
        if len(b)==0:
            b=b+s[i]
        elif s[i]!=b[len(b)-1]:
            b=b+s[i]
        else:
            c+=1
    print(c)
            