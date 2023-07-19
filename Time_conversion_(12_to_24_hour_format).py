s=input()
s1=s[0:2]
s2=s[3:5]
s3=s[6:8]
if s1=='12' and s3=='AM':
    print('00'+':'+s2)
elif s1=='12' and s3=='PM':
    print(s1+':'+s2)
elif s3=='AM':
    print(s1+':'+s2)
elif s3=='PM':
    x=str(int(s1)+12)
    print(x+':'+s2)