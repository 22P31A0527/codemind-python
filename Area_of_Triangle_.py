a,b,c=map(int,input().split())
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))
a1=a**(1/2)
print("%.2f" %a1)