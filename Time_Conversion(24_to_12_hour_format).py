s=input()
s=s.split(':')
s1=s[0]
s2=s[1]
if s1=='00':
    print('12'+':'+s2,'AM')
elif s1=='12':
    print('12'+':'+s2,'PM')
elif int(s1)<12:
    if len(s1)==1:
        print('0'+s1+':'+s2,'AM')
    else:
        print(s1+':'+s2,'AM')
elif int(s1)>12:
    x=str(int(s1)-12)
    if len(x)==1:
        print('0'+x+':'+s2,'PM')
    else:
        print(x+':'+s2,'PM')