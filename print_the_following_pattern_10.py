n=int(input())
for i in range(0,n):
    for l in range(n-1,i,-1):
        print(' ',end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(0,i+1):
        print(k,end="")
    print()