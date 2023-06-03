s=input()
for i in range(0,len(s)):
    x=s.count(s[i])
    if x==1:
        print(i)
        break
else:
    print('-1')