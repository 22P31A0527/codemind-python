n=int(input())
for i in range(1,n+1):
    s=input()
    x='0123456789'
    for i in s:
        if i in x:
            print('Yes')
            break
    else:
        print('No')