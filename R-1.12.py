'''Implementin choice function using randrange function'''
def choic(data):
    return data[(randrange(0,len(data))//randrange(0,len(data)))]
if __name__=='__main__':
    from random import *
    a=[randrange(0,10),randrange(0,10)]
    print(choic(a))