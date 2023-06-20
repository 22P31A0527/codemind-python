s=input()
a=s.count('(')
b=s.count(')')
c=s.count('[')
d=s.count(']')
e=s.count('{')
f=s.count('}')
if (a==b) and (c==d) and (e==f):
    print(True)
else:
    print(False)