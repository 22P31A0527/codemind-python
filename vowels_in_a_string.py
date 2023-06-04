s=input()
a=input()
for i in range(0,len(s)):
    if s[i]==a:
        print(True)
        print(i)
        break
else:
    print(False)