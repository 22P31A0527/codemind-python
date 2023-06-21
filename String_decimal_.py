#57 48
t=int(input())
for k in range(1,t+1):
    n=input()
    for i in range(0,len(n)):
        x=ord(n[i])
        if x<=57 and x>=48:
            continue
        else:
            print(False)
            break
    else:
        print(True)