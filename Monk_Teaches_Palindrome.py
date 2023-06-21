t=int(input())
for k in range(1,t+1):
    s=input()
    if s!=s[::-1]:
        print('NO')
    else:
        if len(s)%2==0:
            print('YES','EVEN')
        else:
            print('YES','ODD')