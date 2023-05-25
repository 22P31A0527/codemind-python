n=int(input())
n1=ord('A')
n2=ord('A')+n
for i in range(n2-1,n1-1,-1):
    for j in range(n1-1,i):
        print(chr(i),end=" ")
    print()