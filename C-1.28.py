'''P-norm of a vector'''
import math
def norm(*v,p=2):
    a=0
    for i in range(len(v)):
        a+=math.pow(v[i],p)
    if(p==2):
        print(math.sqrt(a))
    else:
        print(p*math.sqrt(a))
if __name__=='__main__':
    norm(4,3,p=5)
