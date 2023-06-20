t=int(input())
for k in range(1,t+1):
    n=int(input())
    s=input()
    for i in range(0,n):
        if s.count(s[i])==1:
            print(s[i])
            break
    else:
        print('-1')