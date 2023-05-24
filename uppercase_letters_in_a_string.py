a=input()
x=a
b=a.upper()
c=0
for i in range(len(x)):
    if x[i]==b[i] and x[i]!=' ':
        c+=1
print(c)