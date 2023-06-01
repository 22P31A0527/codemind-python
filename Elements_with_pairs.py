n=int(input())
a=list(map(int,input().split()))
if n%2!=0:
    print(*a,'0')
else:
    print(*a)