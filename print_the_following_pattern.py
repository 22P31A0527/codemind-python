n=int(input())
x=ord('A')
for i in range(x,x+n,1):
    for j in range(x,n+x,1):
        print(chr(i),end=" ")
    print()