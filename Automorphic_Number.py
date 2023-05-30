n1=int(input())
n2=n1*n1
s=1
while n1!=0:
    r1=n1%10
    r2=n2%10
    if r1!=r2:
        s=0
        break
    n1=n1//10
    n2=n2//10
if s==1:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')