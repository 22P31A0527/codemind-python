n=int(input())
a=0
b=1
co=0
while co<n:
    c=a+b
    print(a,end=" ")
    a=b
    b=c
    co+=1