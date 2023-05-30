n=int(input())
a=0
b=1
while a<n:
    c=a+b  
    a=b    
    b=c    
if a==n:
    print(True)
else:
    print(False)