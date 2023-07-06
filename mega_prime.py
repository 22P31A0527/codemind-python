def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        return 1
n=int(input())
s=str(n)
c1=0
if prime(n)==1:
    while n!=0:
        r=n%10
        if prime(r)==1:
            c1=c1+1
        n=n//10
if c1!=len(s):
    print('Not Mega Prime')
else:
    print('Mega Prime')