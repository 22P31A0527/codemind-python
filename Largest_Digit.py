n=int(input())
high=0
while n!=0:
    r=n%10
    if r>high:
        high=r
    n=n//10
print(high)