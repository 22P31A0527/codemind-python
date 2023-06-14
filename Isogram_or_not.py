s=input()
for i in range(0,len(s)):
    if s.count(s[i])!=1:
        print(False)
        break
else:
    print(True)