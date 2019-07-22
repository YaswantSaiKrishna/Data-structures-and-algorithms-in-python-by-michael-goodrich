'''Program to know if integers can be used in correect arthimetic formula'''
a,b,c=input().split()
if(a+b==c and a==b-c and a*b==c):
    print(True)
else:
    print(False)