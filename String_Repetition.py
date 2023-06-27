s=input()
n=int(input())
c1=s.count('a')*(n//len(s))
s1=s[:n%len(s)]
c2=s1.count('a')
print(c1+c2)