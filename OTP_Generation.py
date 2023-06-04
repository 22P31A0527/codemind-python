s=input()
a=[]
for i in s:
    x=int(i)
    if x%2!=0:
        a.append(x*x)
for i in a:
    print(i,end="")