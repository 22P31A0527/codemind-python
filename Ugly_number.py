n=int(input())
s=1
while n!=1:
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    elif n%5==0:
        n=n//5
    else:
        s=0
        break
if s==1:
    print('Ugly Number')
else:
    print('Not Ugly Number')