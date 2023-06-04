s=input()
s=s.lower()
n=s[::-1]
for i in range(0,len(s)):
    if s[i]!=n[i]:
        print(False)
        break
else:
    print(True)