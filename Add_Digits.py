def fun(num):
    s=0
    while(num!=0):
       r=num%10
       s=s+r
       num=num//10
    if s>9:
        s=fun(s)
    return s
n=int(input())
x=fun(n)
print(x)