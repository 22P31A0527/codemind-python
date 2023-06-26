s=input()
if len(s)==10 and s[0]!='0':
    print('Valid')
elif len(s)==11 and s[0]=='0':
    print('Valid')
else:
    print('Invalid')