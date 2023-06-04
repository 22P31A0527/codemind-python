t=int(input())
for i in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if a==b:
        print('0')
    else:
        print(abs(max(b)-min(b)))