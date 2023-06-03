n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    x=i*i
    b.append(x)
b.sort()
print(*b)