n=int(input())
x=ord('A')
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(chr(i+x-1),end=" ")
    print()