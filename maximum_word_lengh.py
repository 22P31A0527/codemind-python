s=input()
s=s.split(' ')
so=0
for i in s:
    if len(i)>so:
        so=len(i)
print(so)