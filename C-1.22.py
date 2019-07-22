'''Dot Product'''
def dot_product(a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c
'''Alternate way
   import numpy as np
   c.append(np.dot(a,b))
'''
if __name__=='__main__':
    print(dot_product([1,2,3],[4,5,6]))
  
