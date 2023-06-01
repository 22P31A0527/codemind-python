def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:return 0
    return 1
n=int(input())
for i in range(1,n+1):
    m=int(input())
    for i in range(m,2*m+1):
        if fun(i)==1:
            a=i
            break
    for i in range(m,0,-1):
        if fun(i)==1:
            b=i
            break
    if abs(m-a)==abs(m-b):
        print(b)
    elif abs(m-a)<abs(m-b):
        print(a)
    else:
        print(b)