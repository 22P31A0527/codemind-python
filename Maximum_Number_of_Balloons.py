s=input()
b=s.count('b')
a=s.count('a')
l=s.count('l')
l=l//2
o=s.count('o')
o=o//2
n=s.count('n')
if b==a==l==o==n:
    print(b)
else:
    k=[b,a,l,o,n]
    mini=b
    for i in range(1,len(k)):
        if k[i]<mini:
            mini=k[i]
    print(mini)