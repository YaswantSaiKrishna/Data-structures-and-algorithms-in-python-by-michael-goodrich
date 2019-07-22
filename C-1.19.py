'''Program to produce list containing ['a'...'z'] using list comprehension'''
print([chr(i) for i in range(65,91)])
print([chr(i) for i in range(97,123)])
'''Alternate way'''
a=ord('A')
b=ord('a')
print([chr(a) for i in range(1,26)])
print([chr(b) for i in range(1,26)])
