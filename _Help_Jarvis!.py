n=int(input())
for i in range(1,n+1):
    m=int(input())
    b=[]
    while m!=0:
        r=m%10
        b.append(r)
        m=m//10
    b.sort()
    for i in range(0,len(b)-1):
        if b[i+1]-b[i]!=1:
           print('NO')
           break
    else:
        print('YES')