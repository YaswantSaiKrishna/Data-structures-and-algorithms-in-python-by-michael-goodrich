'''Distinct numbers'''
def distinct(*data):
    b=set(data)
    return True if(len(b)==len(data)) else False
if __name__=='__main__':
    print(distinct(1,2,3,4,5))
