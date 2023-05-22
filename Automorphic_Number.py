n=int(input())
m=n*n
c=1
while(n!=0):
    r1=n%10
    r2=m%10
    if r1!=r2:
        c=0
        break
    n=n//10
    m=m//10
if c==0:
    print('Not an Automorphic Number')
else:
    print('Automorphic Number')