n=int(input())
arr=list(map(int,input().split()))
i=n-1
while i!=0:
    if arr[i]%2!=0:
        print(arr[i])
        break
    i-=1