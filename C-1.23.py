'''Program to raise exception for IndexError'''
lis=[1,2]
i=2
try:
    print(lis[i])
except IndexError:
    print("\"Don\'t try buffer overflow attacks in python!\"")
