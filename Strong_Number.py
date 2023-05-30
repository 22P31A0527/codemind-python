n=int(input())
s=0
q=n
while n!=0:
   r=n%10
   p=1
   for i in range(1,r+1):
       p=p*i
   s=s+p 
   n=n//10
if s==q:
    print('The number',q,'is a strong number')
else:
    print('The number',q,'is not a strong number')