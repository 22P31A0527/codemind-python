n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    s=sum(a)/len(a)
print(format(s,'.2f'))