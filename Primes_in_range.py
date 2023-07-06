##primes in range
def fun(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if i==1:
        continue
    elif fun(i)==1:
        c=c+1
print(c)