n=int(input())
a=list(map(int,input().split()))
k=int(input())
if a.count(k)==0:
    print('-1')
else:
    print(a.index(k))